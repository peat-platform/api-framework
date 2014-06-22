from common import *

class bcActivity:
    #   region Activity API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Activity%20API/
    
    #   region Event Object
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

    #   endregion Event Object


    #   region Secondary Objects

    #   region Comment Object

    def format_comment_response(self, data):
        response = {
                        "title": data['title'],
                        "text": data['text'],
                        "target_id": data['target_id']
                   }
        response.update(format_generic(data))
        return response

    def delete_a_comment(self, data):
        """ DELETE API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def get_comments_for_account(self, data):
        """ GET API_PATH/[ACCOUNT_ID]/comments """
        return defaultMethodResponse

    #   Checkins
    def get_comments_for_checkin(self, data):
        """ GET API_PATH/[CHECKIN_ID]/comments """
        return defaultMethodResponse

    def post_comment_to_checkin(self, data):
        """ POST API_PATH/[CHECKIN_ID]/comments """
        return defaultMethodResponse

    def delete_a_comment_from_checkin(self, data):
        """ DELETE API_PATH/[CHECKIN_ID]/comments """
        return defaultMethodResponse

    #   Notes
    def get_comments_for_note(self, data):
        """ GET API_PATH/[NOTE_ID]/comments """
        return defaultMethodResponse

    def post_comment_to_note(self, data):
        """ POST API_PATH/[NOTE_ID]/comments """
        return defaultMethodResponse

    def delete_a_comment_from_note(self, data):
        """ DELETE API_PATH/[NOTE_ID]/comments """
        return defaultMethodResponse

    #   Statuses
    def get_comments_for_status(self, data):
        """ GET API_PATH/[STATUS_ID]/comments """
        return defaultMethodResponse

    def post_comment_to_status(self, data):
        """ POST API_PATH/[STATUS_ID]/comments """
        return defaultMethodResponse

    def delete_a_comment_from_status(self, data):
        """ DELETE API_PATH/[STATUS_ID]/comments """
        return defaultMethodResponse

    #   Workouts
    def get_comments_for_workout(self, data):
        """ GET API_PATH/[WORKOUT_ID]/comments """
        return defaultMethodResponse

    def post_comment_to_workout(self, data):
        """ POST API_PATH/[WORKOUT_ID]/comments """
        return defaultMethodResponse

    def delete_a_comment_from_workout(self, data):
        """ DELETE API_PATH/[WORKOUT_ID]/comments """
        return defaultMethodResponse

    #   endregion Comment Object

    #   endregion Secondary Objects

    #   endregion Activity API