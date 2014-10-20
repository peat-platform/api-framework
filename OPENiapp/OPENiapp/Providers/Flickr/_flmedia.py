from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *

class flMedia(bcMedia):
    """ This class is used to:
        1. Get a Flickr Photo
        2. Get all Flickr Photos for an Account

        3. Get all Comments for a Photo
        4. Post a Comment to a Photo
    """
    
    #   region Media API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Media_API
    
    #   region Photo Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Photo_Mapping

    def get_photo(self, id):
        ''' GET API_PATH/[PHOTO_ID] '''
        # /media/media-id (ie media/15124908031)
        photo = self.connector.Photo(id = id)
        raw_data = photo.getInfo()
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon'])
        names.extend(['location_latitude', 'location_longitude', 'location_height'])
        names.extend(['tags', 'height', 'width'])

        fields = ['id', 'media', 'service', 'urls', 'owner.id', '', 'owner.website', 'owner.username', 'taken', 'lastupdate', 'deleted_time']
        fields.extend(['title', 'description', 'originalformat', 'size', 'icon'])
        fields.extend(['location.latitude', 'location.longitude', 'location.height'])
        fields.extend(['tags', 'height', 'width'])

        alternatives = ['', 'photo', 'flickr', '', '', 'account', '', '', '', '', '']
        alternatives.extend(['', '', '', '', ''])
        alternatives.extend(['', '', ''])
        alternatives.extend(['', '', ''])

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
        return response

    def get_photos(self):
        return get_all_photos_for_account('me')

    def get_all_photos_for_account(self, id):
        ''' GET API_PATH/[ACCOUNT_ID]/photos '''
        # /users/username (ie users/chris_dane)
        user = self.connector.Person.findByUserName(id)
        raw_datas = user.getPhotos()
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon'])
        names.extend(['location_latitude', 'location_longitude', 'location_height'])
        names.extend(['tags', 'height', 'width'])

        fields = ['id', 'media', 'service', 'urls', 'owner.id', '', 'owner.website', 'owner.username', 'taken', 'lastupdate', 'deleted_time']
        fields.extend(['title', 'description', 'originalformat', 'size', 'icon'])
        fields.extend(['location.latitude', 'location.longitude', 'location.height'])
        fields.extend(['tags', 'height', 'width'])

        alternatives = ['', 'photo', 'flickr', '', '', 'account', '', '', '', '', '']
        alternatives.extend(['', '', '', '', ''])
        alternatives.extend(['', '', ''])
        alternatives.extend(['', '', ''])

        response = {
                    'meta':
                        {
                         'total_count': len(raw_datas),
                         'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                         'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }

        for raw_data in raw_datas:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_photo_response(data))

        return response

    #   region Connections

    def get_photo_comments(self, id):
        ''' GET API_PATH/[PHOTO_ID]/comments '''
        # /media/media-id/comments (ie media/15124908031/comments)
        photo = self.connector.Photo(id = id)
        raw_datas = photo.getComments()

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text', 'target_id'])

        fields = ['id', 'object_type', 'service', 'permalink', 'author.id', 'author.category', 'author.url', 'author.username', 'datecreate', 'edited_time', 'deleted_time']
        fields.extend(['title', 'text', 'target_id'])

        alternatives = ['', 'comment', 'flickr', '', '', 'account', '', '', '', '', '']
        alternatives.extend(['', '', id])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_comment_response(data))
        return response

    def post_photo_comments(self, id, params):
        ''' POST API_PATH/[PHOTO_ID]/comments '''
        # /media/media-id/comments (ie media/15124908031/comments)
        if (check_if_exists(params, 'comment_text') != defJsonRes):
            photo = self.connector.Photo(id = id)
            return photo.addComment(text = params['comment_text'])
        return "Insufficient Parameters"

    def delete_comment(self, id):
        comment = photo.Comment(id = params['comment_id'])
        return comment.delete()

    #   endregion Connections

    #   endregion Photo Object

    #   endregion Media API
