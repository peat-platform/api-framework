from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *

class fbMedia(bcMedia):
    """ This class is used to:
        1. Get a Facebook User's Photo
        2. Get all Facebook User's Photos
        3. Post Photos to a Facebook User
        4. Get an album's Photos
        4. Post to an album's Photos

        5. Get a Facebook Album as OPENi's folder
    """
    #   region Media API
    
    #   region Photo Object

    def get_a_photo(self, params):
        """ GET API_PATH/[PHOTO_ID] """
        # /photo_id (ie /10153665526210315)
        raw_data = self.connector.get('/' + params['photo_id'])
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longtitude', 'location_height', 'tags', 'height', 'width'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', '', '', 'from.name', 'created_time', 'updated_time', 'deleted_time', 'name', 'description', 'format', 'size', 'icon', 'place.location.latitude', 'place.location.longtitude', 'place.location.height', 'tags.data', 'height', 'width']

        alternatives = ['', 'photo', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'data': [self.format_photo_response(data)]
                    }

        # Curate tag array from Facebook
        tag_array = []
        if (check_if_exists(raw_data, 'tags.data') != defJsonRes):
            for tag in raw_data['tags']['data']:
                    tag_names = ['tags_id', 'tags_name', 'tags_time_created_time', 'tags_time_edited_time', 'tags_time_deleted_time', 'tags_x-location', 'tags_y-location']
                    tag_fields = ['id', 'name', 'created_time', '', '', 'x', 'y']
                    tag_alternatives = ['', '', '', '', '', '', '']
                    tag_data = self.get_fields(tag, tag_names, tag_fields, tag_alternatives)
                    tag_array.append(format_tags(tag_data))
        response['data'][0]['tags'] = tag_array
        
        return response
    
    def get_all_photos_for_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/photos """
        # /account_id/photos (ie /675350314/photos)
        raw_datas = self.connector.get(params['user_id'] +'/photos')
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longtitude', 'location_height', 'tags', 'height', 'width'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', '', '', 'from.name', 'created_time', 'updated_time', 'deleted_time', 'name', 'description', 'format', 'size', 'icon', 'place.location.latitude', 'place.location.longtitude', 'place.location.height', 'tags.data', 'height', 'width']

        alternatives = ['', 'photo', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        response = {
                    'meta':
                        {
                         'total_count': len(raw_datas['data']),
                         'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                         'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }

        for idx, raw_data in enumerate(raw_datas['data']):
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_photo_response(data))

            # Curate tag array from Facebook
            tag_array = []
            if (check_if_exists(raw_data, 'tags.data') != defJsonRes):
                for tag in raw_data['tags']['data']:
                    tag_names = ['tags_id', 'tags_name', 'tags_time_created_time', 'tags_time_edited_time', 'tags_time_deleted_time', 'tags_x-location', 'tags_y-location']
                    tag_fields = ['id', 'name', 'created_time', '', '', 'x', 'y']
                    tag_alternatives = ['', '', '', '', '', '', '']
                    tag_data = self.get_fields(tag, tag_names, tag_fields, tag_alternatives)
                    tag_array.append(format_tags(tag_data))
            response['data'][idx]['tags'] = tag_array
        
        return response

    def post_photo_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/photos """
        # /account_id/photos (ie /675350314/photos)
        if (check_if_exists(params, 'user_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                return self.connector.post(path = self.params.user_id+'/photos', source = open(self.params.path_string, 'rb'))
            elif (check_if_exists(params, 'url') != defJsonRes):
                return self.connector.post(path = self.params.user_id+'/photos', url = open(self.params.url, 'rb'))
        return "Insufficient Parameters"
    
    def get_all_photos_for_album(self, params):
        """ Get all photos for an album """
        # /album_id/photos (ie /10150259489830315/photos)
        raw_datas = self.connector.get(params['album_id'] +'/photos')
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longtitude', 'location_height', 'tags', 'height', 'width'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', '', '', 'from.name', 'created_time', 'updated_time', 'deleted_time', 'name', 'description', 'format', 'size', 'icon', 'place.location.latitude', 'place.location.longtitude', 'place.location.height', 'tags.data', 'height', 'width']

        alternatives = ['', 'photo', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        response = {
                    'meta':
                        {
                         'total_count': len(raw_datas['data']),
                         'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                         'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }

        for idx, raw_data in enumerate(raw_datas['data']):
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_photo_response(data))

            # Curate tag array from Facebook
            tag_array = []
            if (check_if_exists(raw_data, 'tags.data') != defJsonRes):
                for tag in raw_data['tags']['data']:
                    tag_names = ['tags_id', 'tags_name', 'tags_time_created_time', 'tags_time_edited_time', 'tags_time_deleted_time', 'tags_x-location', 'tags_y-location']
                    tag_fields = ['id', 'name', 'created_time', '', '', 'x', 'y']
                    tag_alternatives = ['', '', '', '', '', '', '']
                    tag_data = self.get_fields(tag, tag_names, tag_fields, tag_alternatives)
                    tag_array.append(format_tags(tag_data))
            response['data'][idx]['tags'] = tag_array
        
        return response
        
    def post_photo_to_album(self, data):
        """ POST API_PATH/[ALBUM_ID]/photos """
        # /album_id/photos (ie /10150259489830315/photos)
        if (check_if_exists(params, 'album_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                return self.connector.post(path = self.params.album_id+'/photos', source = open(self.params.path_string, 'rb'))
            elif (check_if_exists(params, 'url') != defJsonRes):
                return self.connector.post(path = self.params.album_id+'/photos', url = open(self.params.url, 'rb'))
        return "Insufficient Parameters"

    def delete_a_photo(self, params):
        """ DELETE API_PATH/[PHOTO_ID] """
        # /photo_id (ie /10153665526210315)
        if (check_if_exists(params, 'photo_id') != defJsonRes):
            return self.connector.delete(self.params.photo_id)
        return "Insufficient Parameters"
    

    #   region Connections
    
    def get_comments(self, params):
        """ Get comments for a photo by its id """
        return self.connector.get(self.params.photo_id+'/comments')
    
    def post_comment(self, params):
        """ Post a comment to a photo by its id """
        return self.connector.post(path = self.params.photo_id+'/comments', data = self.data.comment)
    
    def delete_comment(self, params):
        """ Delete a comment by its id """
        return self.connector.delete(self.params.comment_id)
    
    def edit_comment(self, params):
        """ Edit a comment by its id """
        # This would be possible only by deleting the comment and creating a new one.
        return {'result': 'Not applicable'}
    
    def like_photo(self, params):
        """ Like a photo by its id """
        return self.connector.post(self.params.photo_id + '/likes')
    
    def get_likes_for_photo(self, params):
        """ Get like for a photo by its id """
        return self.connector.get(self.params.photo_id + '/likes')
    
    def unlike_photo(self, data):
        """ Unlike a photo by its id """
        return self.connector.delete(self.params.photo_id + '/likes')
    
    def dislike_photo(self, data):
        """ Dislike a photo by its id """
        return {'result': 'Not applicable'}
    
    def get_dislikes_for_article(self, params):
        """ Get dislikes for an article """
        return {'result': 'Not applicable'}
    
    def delete_photo_from_article(self, params):
        """ Delete a photo from an article """
        return {'result': 'Not applicable'}

    #   endregion Connections

    #   endregion Photo Object
    


    #   region Folder Aggregation 
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Folder%20Mapping

    def get_a_folder(self, params):
        """ GET API_PATH/[FOLDER_ID] """
        # /album_id (ie /10153665525255315)
        raw_data = self.connector.get('/' + params['album_id'])
        raw_data2 = self.connector.get('/' + params['album_id'] + '/photos')
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'data'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', '', '', 'from.name', 'created_time', 'updated_time', 'deleted_time', 'name', 'description', 'format', 'size', 'icon', 'data']

        alternatives = ['', 'album', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'data': [self.format_folder_response(data)]
                    }
        response['data'][0]['data'] = self.get_all_photos_for_album({'album_id': params['album_id']})
        return response
    
    def post_folder_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID] """
        # /account_id (ie /675350314)
        if (check_if_exists(params, 'account_id') != defJsonRes):
            return self.connector.post(
                    '/' + params['account_id'] + '/albums',
                    name = data['name'],
                    message = check_if_exists(params, 'message', ''),
                    privacy = check_if_exists(params, 'privacy', {}))
        return "Insufficient Parameters"

    #   endregion Folder Aggregation

    #   endregion Media API