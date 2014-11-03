from OPENiapp.Providers.base.activity import bcActivity
from OPENiapp.Providers.base.common import *

class foActivity(bcActivity):
    """ This class is used to:
        1. Get a Foursquare Event
    """
    #   region Activity API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Activity_API
    
    #   region Event Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Event_Mapping
    
    def get_event(self, id):
        """ GET API_PATH/[EVENT_ID] """
        # /event_id (ie /4e173d2cbd412187aabb3c04)
        raw_data = self.connector.events(id)
        
        names = ['id', 'object_type', 'service', 'resource_uri', 'from_id', 'from_object_type', 'from_resource_uri', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['place_name', 'place_description', 'place_category', 'place_picture', 'place_address_street', 'place_address_number', 'place_address_apartment', 'place_address_city', 'place_address_locality', 'place_address_country', 'place_address_zip', 'place_location_latitude', 'place_location_longitude', 'place_location_height'])
        names.extend(['duration_starts_time', 'duration_ends_time'])
        names.extend(['description', 'picture', 'title'])

        fields = ['id', 'object_type', 'service', 'url', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['location', '', '', '', '', '', '', '', '', '', '', 'venue.latitude', 'venue.longitude', ''])
        fields.extend(['startAt', 'endAt'])
        fields.extend(['description', 'picture', 'name'])

        alternatives = ['', 'event', 'foursquare', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', '', '', '', '', '', '', '', '', '', '', '', ''])
        alternatives.extend(['', ''])
        alternatives.extend(['', '', ''])

        data = self.get_fields(raw_data['event'], names, fields, alternatives)
        response = {
            'meta': {
                'limit': self.check_if_exists(raw_datas, 'limit', None),
                'next': self.check_if_exists(raw_datas, 'paging.next', None),
                'offset': self.check_if_exists(raw_datas, 'offset', 0),
                'previous': self.check_if_exists(raw_datas, 'paging.previous', None),
                'total_count': self.check_if_exists(raw_datas, 'total_count', 1)
            },
            'objects': [self.format_event_response(data)]
        }
        
        venue_id = self.check_if_exists(raw_data, 'event.venueId')
        if (venue_id != defJsonRes):
            raw_data2 = self.connector.venues(venue_id)
            response['objects'][0]['place']['name'] = self.check_if_exists(raw_data2, 'venue.name', '')
            response['objects'][0]['place']['description'] = self.check_if_exists(raw_data2, 'venue.description', '')
            response['objects'][0]['place']['category'] = self.check_if_exists(raw_data2, 'venue.categories', '')
            response['objects'][0]['place']['picture'] = self.check_if_exists(raw_data2, 'venue.photos', '')
            response['objects'][0]['place']['address']['street'] = self.check_if_exists(raw_data2, 'venue.location.address', '')
            response['objects'][0]['place']['address']['number'] = self.check_if_exists(raw_data2, 'venue.location.number', '')
            response['objects'][0]['place']['address']['apartment'] = self.check_if_exists(raw_data2, 'venue.location.apartment', '')
            response['objects'][0]['place']['address']['city'] = self.check_if_exists(raw_data2, 'venue.location.city', '')
            response['objects'][0]['place']['address']['locality'] = self.check_if_exists(raw_data2, 'venue.location.locality', '')
            response['objects'][0]['place']['address']['country'] = self.check_if_exists(raw_data2, 'venue.location.country', '')
            response['objects'][0]['place']['address']['zip'] = self.check_if_exists(raw_data2, 'venue.location.postalCode', '')
            response['objects'][0]['place']['address']['latitude'] = self.check_if_exists(raw_data2, 'venue.location.lat', '')
            response['objects'][0]['place']['address']['longitude'] = self.check_if_exists(raw_data2, 'venue.location.lng', '')
            response['objects'][0]['place']['address']['height'] = self.check_if_exists(raw_data2, 'venue.location.height', '')

        return response

    def get_checkins(self):
        """ GET API_PATH/[ACCOUNT_ID] """
        return self.connector.users.checkins()
    
    #   region Connections


    #   endregion Connections

    #   endregion Event Object

    #   endregion Activity API