from common import *

class bcActivity:
    #   region Activity API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Activity%20API/
    
    #   region Badge Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Badge%20Mapping/

    def format_event_response(self, data):
        response = {
                        "place":{
                            "name": data['place_name'],
                            "description": data['place_description'],
                            "category": data['place_category'],
                            "address":{
                                "street": data['place_address_street'],
                                "number": data['place_address_number'],
                                "apartment": data['place_address_apartment'],
                                "city": data['place_address_city'],
                                "locality": data['place_address_locality'],
                                "country": data['place_address_country'],
                                "zip": data['place_address_zip']
                                },
                            "location":{
                                "latitude": data['place_location_latitude'],
                                "longtitude": data['place_location_longitude'],
                                "height": data['place_location_height']
                                }
                        },
                        "duration":{
                                "starts_time": data['duration_starts_time'],
                                "ends_time": data['duration_ends_time']
                        },
                        "description": data['description'],
                        "picture": data['picture'],
                        "title": data['title']
                   }
        response.update(format_generic(data))
        return response
    
    def get_an_event(self, data):
        """ GET API_PATH/[EVENT_ID] """
        return defaultMethodResponse

    def get_all_events_for_account(self, data):
        """ GET API_PATH/[ACCOUNT_ID]/events """
        return defaultMethodResponse

    def post_event_to_account(self, data):
        """ POST API_PATH/[ACCOUNT_ID]/events """
        return defaultMethodResponse
        
    def post_event_to_aggregation(self, data):
        """ POST API_PATH/[AGGREGATION_ID]/events """
        return defaultMethodResponse

    def edit_an_event(self, data):
        """ PUT API_PATH/[EVENT_ID] """
        return defaultMethodResponse

    def delete_an_event(self, data):
        """ DELETE API_PATH/[EVENT_ID] """
        return defaultMethodResponse

    #   endregion Badge Object


    #   region Secondary Objects

    #   endregion Secondary Objects

    #   endregion Activity API