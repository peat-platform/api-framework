from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *

class inMedia(bcMedia):
    """ This class is used to:
        1. Get an Instagram Photo
        2. Get all Instagram Photos for an Account
    """
    #   region Media API
    
    #   region Photo Object

    def get_a_photo(self, params):
        # /media/media-id (ie media/628147512937366504_917877895)
        raw_data = self.connector.media(params['media_id'])
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon'])
        names.extend(['location_latitude', 'location_longitude', 'location_height'])
        names.extend(['tags', 'height', 'width'])

        fields = ['id', 'object_type', 'service', 'link', 'user.id', 'user.object_type', 'user.website', 'user.username', 'created_time', 'updated_time', 'deleted_time']
        fields.extend(['caption', 'description', 'format', 'size', 'suffix'])
        fields.extend(['location.point.latitude', 'location.point.longitude', 'location.point.height'])
        fields.extend(['tags', 'images.standard_resolution.height', 'images.standard_resolution.width'])
        
        alternatives = ['', 'photo', 'foursquare', '', '', 'account', '', '', '', '', '']
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