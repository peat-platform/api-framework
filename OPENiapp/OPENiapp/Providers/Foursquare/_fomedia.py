from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *

class foMedia(bcMedia):
    """ This class is used to:
        1. Get a Foursquare Photo
        2. Get all Foursquare Photos for an Account
    """
    #   region Media API
    
    #   region Photo Object

    def get_a_photo(self, params):
        ''' GET API_PATH/[PHOTO_ID] '''
        # /media/media-id (ie media/628147512937366504_917877895)
        raw_data = self.connector.photos(params['photo_id'])
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon'])
        names.extend(['location_latitude', 'location_longitude', 'location_height'])
        names.extend(['tags', 'height', 'width'])

        fields = ['id', 'object_type', 'service', 'link', 'user.id', 'user.object_type', 'user.website', 'user.firstName', 'created_at', 'updated_time', 'deleted_time']
        fields.extend(['venue.name', 'description', 'format', 'size', 'suffix'])
        fields.extend(['venue.location.lat', 'venue.location.lng', 'venue.location.height'])
        fields.extend(['tags.data', 'height', 'width'])
        
        alternatives = ['', 'photo', 'foursquare', '', '', 'account', '', '', '', '', '']
        alternatives.extend(['', '', '', '', ''])
        alternatives.extend(['', '', ''])
        alternatives.extend(['', '', ''])

        data = self.get_fields(raw_data['photo'], names, fields, alternatives)
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

    def get_all_photos_for_account(self, data):
        ''' GET API_PATH/[ACCOUNT_ID]/photos '''
        # /users/user-id (ie users/917877895)
        raw_datas = self.connector.users.photos('self')
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon'])
        names.extend(['location_latitude', 'location_longitude', 'location_height'])
        names.extend(['tags', 'height', 'width'])

        fields = ['id', 'object_type', 'service', 'link', 'user.id', 'user.object_type', 'user.website', 'user.firstName', 'created_at', 'updated_time', 'deleted_time']
        fields.extend(['venue.name', 'description', 'format', 'size', 'suffix'])
        fields.extend(['venue.location.lat', 'venue.location.lng', 'venue.location.height'])
        fields.extend(['tags.data', 'height', 'width'])
        
        alternatives = ['', 'photo', 'foursquare', '', '', 'account', '', '', '', '', '']
        alternatives.extend(['', '', '', '', ''])
        alternatives.extend(['', '', ''])
        alternatives.extend(['', '', ''])

        response = {
                    'meta': 
                        {
                        'total_count': self.check_if_exists(raw_datas, 'photos.count'),
                        'next': self.check_if_exists(raw_datas, 'photos.next')
                        },
                    'data' : [] }
        for raw_data in raw_datas['photos']['items']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_photo_response(data))

        return response

    #   region Connections

    #   endregion Connections

    #   endregion Photo Object

    #   endregion Media API