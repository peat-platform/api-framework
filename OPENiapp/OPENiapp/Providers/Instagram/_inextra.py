from OPENiapp.Providers.base.common import *

class inExtra():
    def search_media(self, params):
        ''' GET API_PATH/ '''
        raw_data = self.connector.media_search(lat = params['lat'], lng = params['lng'])
        
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

        response = []
        for raw_dato in raw_data:
            data = self.get_fields(raw_dato, names, fields, alternatives)
            response.append(self.format_photo_response(data))
        return {'response': response}

    def filter_tags_photos(self, params):
        raw_data = self.search_media(params)['response']
        response = []

        for idx, dat in enumerate(raw_data):
            for tag in dat['tags']:
                for tag2 in params['tags']:
                    if (tag.name == tag2) and (raw_data[idx] not in response):
                        response.append(raw_data[idx])
                        break
        
        return response