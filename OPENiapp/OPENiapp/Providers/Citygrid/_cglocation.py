from OPENiapp.Providers.base.location import bcLocation
from OPENiapp.Providers.base.common import *

import json

class cgLocation(bcLocation):
    """ This class is used to:
        1. Get a CityGrid Place
    """

    #   region Location API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Location_API
    
    #   region Place Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Place%20Mapping/

    def get_a_place(self, params):
        """ GET API_PATH/[PLACE_ID] """
        # Returns a detailed instance of Citygrid
        #https://api.citygridmedia.com/content/places/v2/detail?id=10100230&id_type=cs&placement=search_page&client_ip=123.4.56.78&publisher=test&format=json
        raw_data = self.connector.placesdetail(id = self.check_if_exists(params ,'id', ''),
                                            id_type = self.check_if_exists(params ,'id_type', ''),
                                            phone = self.check_if_exists(params ,'phone', ''),
                                            publishercode = self.check_if_exists(params ,'publisher', ''),
                                            customer_only = self.check_if_exists(params ,'customer_only', ''),
                                            all_results = self.check_if_exists(params, 'all_results', ''),
                                            review_count = self.check_if_exists(params ,'review_count', ''),
                                            placement = self.check_if_exists(params ,'placement', ''),
                                            #client_ip = params['client_ip'],
                                            format = self.check_if_exists(params ,'format', ''),
                                            callback = self.check_if_exists(params ,'callback', ''),
                                            i = self.check_if_exists(params ,'i', ''))
        raw_data = json.loads(raw_data)['locations'][0]
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['place_name', 'place_description', 'place_category', 'place_picture', 'place_address_street', 'place_address_number', 'place_address_apartment', 'place_address_city', 'place_address_locality', 'place_address_country', 'place_address_zip', 'place_location_latitude', 'place_location_longitude', 'place_location_height'])
        names.extend(['text'])

        fields = ['id', 'type', 'service', 'urls.profile_url', 'user.id', 'user.category', 'contact_info.display_url', 'user.username', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['name', '', 'types', '', 'address.street', 'address.number', '', '', '', '', '', 'address.latitude', 'address.longitude', ''])
        fields.extend(['name'])

        alternatives = ['', 'place', 'CityGrid', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', '', '', '', '', '', '', '', '', '', '', '', ''])
        alternatives.extend([''])
        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': [self.format_place_response(data)]
                    }
        return response

    #   endregion Place Object

    #   endregion Location API