from common import *

class bcProductsServices:
    #   region Products And Services API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Profiles%20API/
    
    #   region Application Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Application%20Mapping/

    def format_application_response(self, data):
        response = {
                        "application": format_application(data),
                        "adtype": data['adtype'],
                        "adservices" : data['adservices'],
                        "adnetworks" : data['adnetworks']
                   }
        response.update(format_generic(data))
        return response
    
    #def get_an_application(self, data):
    def get_application(self, id):
        """ GET API_PATH/[APP_ID] """
        return defaultMethodResponse
    
    #def get_all_applications_for_account(self, data):
    def get_applications(self):
        """ GET API_PATH/[ACCOUNT_ID]/applications """
        return defaultMethodResponse

    #def get_profile_for_user(self, data):
    #    """ GET API_PATH/[USER_ID]/applications """
    #    return defaultMethodResponse
    
    #def post_application_to_account(self, data):
    def post_applications(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/applications """
        return defaultMethodResponse
        
    #def post_application_to_aggregation(self, data):
    #    """ POST API_PATH/[AGGREGATION_ID]/applications """
    #    return defaultMethodResponse
    
    #def edit_an_application(self, data):
    def put_application(self, id, params):
        """ PUT API_PATH/[APP_ID] """
        return defaultMethodResponse
    
    #def delete_an_application(self, data):
    def delete_application(self, id):
        """ DELETE API_PATH/[APP_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_application_comments(self, id):
        """ GET API_PATH/[APP_ID]/comments """
        return defaultMethodResponse

    def post_application_comments(self, id, params):
        """ POST API_PATH/[APP_ID]/comments """
        return defaultMethodResponse

    def post_application_likes(self, id):
        """ POST API_PATH/[APP_ID]/likes """
        return defaultMethodResponse

    def get_application_likes(self, id):
        """ GET API_PATH/[APP_ID]/likes """
        return defaultMethodResponse

    def delete_application_likes(self, id):
        """ DELETE API_PATH/[APP_ID]/likes """
        return defaultMethodResponse

    def post_application_dislikes(self, id):
        """ POST API_PATH/[APP_ID]/dislikes """
        return defaultMethodResponse

    def get_application_dislikes(self, id):
        """ GET API_PATH/[APP_ID]/dislikes """
        return defaultMethodResponse

    def delete_application_dislikes(self, id):
        """ DELETE API_PATH/[APP_ID]/dislikes """
        return defaultMethodResponse


    #   endregion Connections

    #   endregion Application Object


    #   region Secondary Objects

    #   region Score Object

    def format_score_response(self, data):
        response = {
                        "value": data['value'],
                        "target_id": data['target_id'],
                   }
        response.update(format_generic(data))
        return response
    
    #def get_scores_from_account(self, data):
    def get_scores(self):
        """ GET API_PATH/{ACCOUNT_ID}/scores """
        return defaultMethodResponse

    #def get_scores_from_user(self, data):
    #    """ GET API_PATH/{USER_ID}/scores """
    #    return defaultMethodResponse
    
    #def get_scores_from_game(self, data):
    def get_game_scores(self, id):
        """ GET API_PATH/{GAME_ID}/scores """
        return defaultMethodResponse
    
    #def post_score_to_account(self, data):
    def post_scores(self, id, params):
        """ POST API_PATH/{GAME_ID}/scores """
        return defaultMethodResponse
    
    #def delete_all_scores_from_game(self, data):
    def delete_game_scores(self, id):
        """ DELETE API_PATH/{GAME_ID}/scores """
        return defaultMethodResponse

    #   endregion Score Objects

    #   endregion Secondary Objects

    #   endregion Products And Services API