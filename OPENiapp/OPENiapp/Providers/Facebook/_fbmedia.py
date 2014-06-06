from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *

class fbMedia(bcMedia):
    """ This class is used to:
        1. Get a Facebook User's Photo
        2. Get all Facebook User's Photos
        3. Post Photos to a Facebook User
        4. Get an album's Photos

        5. Get a Facebook Album as OPENi's folder
    """
    #   region Media API
    
    #   region Photo Object

    def get_a_photo(self, params):
        """ Get a photo by its id """
        # /photo_id (ie /10153665526210315)
        raw_data = self.connector.get('/' + params['photo_id'])

        names = ['id', 'object_type', 'service', 'url', 'file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'from_id', 'from_name', 'from_surname', 'from_middlename', 'from_birthdate', 'from_organizations', 'location_latitude', 'location_longtitude', 'location_height', 'tags', 'created_time', 'edited_time', 'deleted_time', 'height', 'width']

        fields = ['id', 'object_type', 'service', 'link', 'name', 'description', 'format', 'size', 'icon', 'from.id', 'from.name', 'from.surname', 'from.middlename', 'from.birthdate', 'from.organizations', 'place.location.latitude', 'place.location.longtitude', 'place.location.height', 'tags.data', 'created_time', 'updated_time', 'deleted_time', 'height', 'width']

        alternatives = ['', 'photo', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': self.format_photo_response(data)
                    }

        # Curate tag array from Facebook
        tag_array = []
        if (check_if_exists(raw_data, 'tags.data') != defJsonRes):
            for tag in raw_data['tags']['data']:
                    tag_names = ['id', 'name', 'time_created_time', 'time_edited_time', 'time_deleted_time', 'x-location', 'y-location']
                    tag_fields = ['id', 'name', 'created_time', '', '', 'x', 'y']
                    tag_alternatives = ['', '', '', '', '', '', '']
                    tag_data = self.get_fields(tag, tag_names, tag_fields, tag_alternatives)
                    tag_array.append(format_tags(tag_data))
        response['data']['tags'] = tag_array
        
        return { 'response': response }
    
    def get_all_photos_for_account(self, params):
        """ Get all photos for an account """
        # /account_id (ie /675350314/photos)
        raw_datas = self.connector.get(params['user_id'] +'/photos')

        names = ['id', 'object_type', 'service', 'url', 'file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'from_id', 'from_name', 'from_surname', 'from_middlename', 'from_birthdate', 'from_organizations', 'location_latitude', 'location_longtitude', 'location_height', 'tags', 'created_time', 'edited_time', 'deleted_time', 'height', 'width']

        fields = ['id', 'object_type', 'service', 'link', 'name', 'description', 'format', 'size', 'icon', 'from.id', 'from.name', 'from.surname', 'from.middlename', 'from.birthdate', 'from.organizations', 'place.location.latitude', 'place.location.longtitude', 'place.location.height', 'tags.data', 'created_time', 'updated_time', 'deleted_time', 'height', 'width']

        alternatives = ['', 'photo', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

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
                    tag_names = ['id', 'name', 'time_created_time', 'time_edited_time', 'time_deleted_time', 'x-location', 'y-location']
                    tag_fields = ['id', 'name', 'created_time', '', '', 'x', 'y']
                    tag_alternatives = ['', '', '', '', '', '', '']
                    tag_data = self.get_fields(tag, tag_names, tag_fields, tag_alternatives)
                    tag_array.append(format_tags(tag_data))
            response['data'][idx]['tags'] = tag_array
        
        return { 'response': response }

    def post_photo_to_account(self, params):
        """ Post a photo to a simple account """
        return self.connector.post(path = self.params.user_id+'/photos', source = open(self.params.path_string, 'rb'))
    
    def get_all_photos_for_album(self, params):
        """ Get all photos for an album """
        # /album_id (ie /10150259489830315/photos)
        raw_datas = self.connector.get(params['album_id'] +'/photos')

        names = ['id', 'object_type', 'service', 'url', 'file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'from_id', 'from_name', 'from_surname', 'from_middlename', 'from_birthdate', 'from_organizations', 'location_latitude', 'location_longtitude', 'location_height', 'tags', 'created_time', 'edited_time', 'deleted_time', 'height', 'width']

        fields = ['id', 'object_type', 'service', 'link', 'name', 'description', 'format', 'size', 'icon', 'from.id', 'from.name', 'from.surname', 'from.middlename', 'from.birthdate', 'from.organizations', 'place.location.latitude', 'place.location.longtitude', 'place.location.height', 'tags.data', 'created_time', 'updated_time', 'deleted_time', 'height', 'width']

        alternatives = ['', 'photo', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

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
                    tag_names = ['id', 'name', 'time_created_time', 'time_edited_time', 'time_deleted_time', 'x-location', 'y-location']
                    tag_fields = ['id', 'name', 'created_time', '', '', 'x', 'y']
                    tag_alternatives = ['', '', '', '', '', '', '']
                    tag_data = self.get_fields(tag, tag_names, tag_fields, tag_alternatives)
                    tag_array.append(format_tags(tag_data))
            response['data'][idx]['tags'] = tag_array
        
        return { 'response': response }

    def share_photo(self, params):
        """ Share a photo """
        return {'result': 'Not applicable'}

    def edit_photo_object(self, params):
        """ Edit a photo object """
        return {'result': 'Not applicable'}

    def delete_photo_object(self, params):
        """ Delete a photo object """
        return self.connector.delete(self.params.photo_id)
    

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

        names = ['id', 'object_type', 'service', 'url', 'file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'from_id', 'from_name', 'from_surname', 'from_middlename', 'from_birthdate', 'from_organizations', 'created_time', 'edited_time', 'deleted_time', 'data']
        fields = ['id', 'object_type', 'service', 'link', 'name', 'description', 'format', 'size', 'icon', 'from.id', 'from.name', 'from.surname', 'from.middlename', 'from.birthdate', 'from.organizations', 'created_time', 'updated_time', 'deleted_time', 'data']
        alternatives = ['', 'album', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': self.format_folder_response(data)
                    }
        response['data']['data'] = self.get_all_photos_for_album({'album_id': params['album_id']})
        return { 'response': response }
    
    def post_folder_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID] """
        # /account_id (ie /675350314)
        response = self.connector.post(
            '/' + params['account_id'] + '/albums',
            name = data['name'],
            message = check_if_exists(params, 'message', ''),
            privacy = check_if_exists(params, 'privacy', {}))
        return { 'response': response }

    #   endregion Folder Aggregation

    #   endregion Media API