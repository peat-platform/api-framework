from OPENiapp.Providers.base.activity import bcActivity
from OPENiapp.Providers.base.common import *

class fbActivity(bcActivity):
    """ This class is used to:
        1. Get a Facebook Event
        2. Get all Events for a Facebook Account
    """
    #   region Location API
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Location_API
    
    #   region Event Object
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Event_Mapping
    
    def get_an_event(self, data):
        """ GET API_PATH/[EVENT_ID] """
        # /event_id (ie /577733618968497)
        raw_data = self.connector.get(data['event_id'])
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['place_name', 'place_description', 'place_category', 'place_address_street', 'place_address_number', 'place_address_apartment', 'place_address_city', 'place_address_locality', 'place_address_country', 'place_address_zip', 'place_location_latitude', 'place_location_longitude', 'place_location_height', 'duration_starts_time', 'duration_ends_time', 'description', 'picture', 'title'])

        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time', 'location', '', '', '', '', '', '', '', '', '', 'venue.latitude', 'venue.longitude', '', 'start_time', 'end_time', 'description', 'picture', 'name']

        alternatives = ['', 'event', 'openi', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'data': [self.format_event_response(data)]
                    }
        return response

    def get_all_events_for_account(self, data):
        """ GET API_PATH/[ACCOUNT_ID]/events """
        raw_datas = self.connector.get('/' + data['user_id'] + '/events')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['place_name', 'place_description', 'place_category', 'place_address_street', 'place_address_number', 'place_address_apartment', 'place_address_city', 'place_address_locality', 'place_address_country', 'place_address_zip', 'place_location_latitude', 'place_location_longitude', 'place_location_height', 'duration_starts_time', 'duration_ends_time', 'description', 'picture', 'title'])

        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time', 'location', '', '', '', '', '', '', '', '', '', 'venue.latitude', 'venue.longitude', '', 'start_time', 'end_time', 'description', 'picture', 'name']

        alternatives = ['', 'event', 'openi', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas['data']),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_event_response(data))
        return response
    
    #   region Connections


    #   endregion Connections

    #   endregion Event Object

    #   endregion Location API