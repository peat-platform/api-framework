from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *

class inMedia(bcMedia):
    """ This class is used to:
        1. Get an Instagram Photo
        2. Get all Instagram Photos for an Account
    """
    #   region Media API
    
    #   region Photo Object

    def get_photo(self, id):
        # /media/media-id (ie media/628147512937366504_917877895)
        raw_data = self.connector.media(id)
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon'])
        names.extend(['location_latitude', 'location_longitude', 'location_height'])
        names.extend(['tags', 'height', 'width'])

        fields = ['id', 'object_type', 'service', 'link', 'user.id', 'user.object_type', 'user.website', 'user.username', 'created_time', 'updated_time', 'deleted_time']
        fields.extend(['caption', 'description', 'format', 'size', 'suffix'])
        fields.extend(['location.point.latitude', 'location.point.longitude', 'location.point.height'])
        fields.extend(['tags', 'images.standard_resolution.height', 'images.standard_resolution.width'])
        
        alternatives = ['', 'photo', 'instagram', '', '', 'account', '', '', '', '', '']
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
        return self.get_all_photos_for_account('me')

    def get_all_photos_for_account(self, id):
        ''' GET API_PATH/[ACCOUNT_ID]/photos '''
        # /users/user-id (ie users/917877895)
        raw_datas, next = self.connector.user_recent_media(id)
        if (next == None):
            next = defJsonRes
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon'])
        names.extend(['location_latitude', 'location_longitude', 'location_height'])
        names.extend(['tags', 'height', 'width'])

        fields = ['id', 'object_type', 'service', 'link', 'user.id', 'user.object_type', 'user.website', 'user.username', 'created_time', 'updated_time', 'deleted_time']
        fields.extend(['caption', 'description', 'format', 'size', 'suffix'])
        fields.extend(['location.point.latitude', 'location.point.longitude', 'location.point.height'])
        fields.extend(['tags', 'images.standard_resolution.height', 'images.standard_resolution.width'])
        
        alternatives = ['', 'photo', 'instagram', '', '', 'account', '', '', '', '', '']
        alternatives.extend(['', '', '', '', ''])
        alternatives.extend(['', '', ''])
        alternatives.extend(['', '', ''])

        response = {
                    'meta':
                        {
                         'total_count': len(raw_datas),
                         'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                         'next': next
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
        # /media/media-id/comments (ie media/628147512937366504_917877895/comments)
        raw_datas = self.connector.media_comments(id)

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text', 'target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', 'from.category', 'from.url', 'from.username', 'created_time', 'edited_time', 'deleted_time']
        fields.extend(['title', 'text', 'target_id'])

        alternatives = ['', 'comment', 'Instagram', '', '', '', '', '', '', '', '']
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
            response['data'].append(format_comment_response(data))
        return response
    
    def post_photo_comments(self, id):
        """ POST API_PATH/[PHOTO_ID]/comments """
        # /media/media-id/comments (ie media/628147512937366504_917877895/comments)
        # 'error_message': 'Please visit http://bit.ly/instacomments for commenting access' Please email apidevelopers[at]instagram.com for access.
        return defaultMethodResponse

    def delete_comment(self, id):
        ''' DELETE API_PATH/[COMMENT_ID] '''
        return self.connector.delete_comment(id)

    def post_photo_likes(self, id):
        ''' POST API_PATH/[PHOTO_ID]/likes '''
        # /media/media-id/likes (ie media/628147512937366504_917877895/likes)
        return self.connector.like_media(id)

    def get_photo_likes(self, id):
        ''' GET API_PATH/[PHOTO_ID]/likes '''
        # /media/media-id/likes (ie media/628147512937366504_917877895/likes)
        raw_datas = self.connector.media_likes(id)

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'id', 'category', 'url', 'from.username', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['target_id'])

        alternatives = ['', 'like', 'Instagram', '', '', '', '', '', '', '', '']
        alternatives.extend([id])

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
            response['data'].append(format_likes_response(data))
        return response

    def delete_photo_likes(self, id):
        ''' DELETE API_PATH/[PHOTO_ID]/likes '''
        # /media/media-id/likes (ie media/628147512937366504_917877895/likes)
        return self.connector.unlike_media(id)

    #   endregion Connections

    #   endregion Photo Object

    #   endregion Media API