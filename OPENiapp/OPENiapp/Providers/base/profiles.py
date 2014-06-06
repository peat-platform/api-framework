from common import *

class bcProfiles:
    #   region Profiles API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Profiles%20API/
    
    #   region Application Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Application%20Mapping/

    def format_application_response(self, data):
        response = {
                        "id": data['id'],
                        "objectType": data['object_type'],
                        "service": data['service'],
                        "url": data['url'],
                        "application":{
                               "title": data['application_title'],
                               "description": data['application_description'],
                               "version": data['application_version'],
                               "icon": data['application_icon'],
                               "developer": data['application_developer']
                               },
                        "adtype": data['adtype'],
                        "adservices" : data['adservices'],
                        "adnetworks" : data['adnetworks']
                   }
        return response
    
    def get_an_application(self, data):
        """ GET API_PATH/[APP_ID] """
        return defaultMethodResponse

    def get_all_applications_for_account(self, data):
        """ GET API_PATH/[ACCOUNT_ID]/applications """
        return defaultMethodResponse

    def get_profile_for_user(self, data):
        """ GET API_PATH/[USER_ID]/applications """
        return defaultMethodResponse

    def post_application_to_account(self, data):
        """ POST API_PATH/[ACCOUNT_ID]/applications """
        return defaultMethodResponse
        
    def post_application_to_aggregation(self, data):
        """ POST API_PATH/[AGGREGATION_ID]/applications """
        return defaultMethodResponse

    def edit_an_application(self, data):
        """ PUT API_PATH/[APP_ID] """
        return defaultMethodResponse

    def delete_an_application(self, data):
        """ DELETE API_PATH/[APP_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_application_comments(self, data):
        """ GET API_PATH/[APP_ID]/comments """
        return defaultMethodResponse

    def post_application_comment(self, data):
        """ POST API_PATH/[APP_ID]/comments """
        return defaultMethodResponse

    def delete_application_comment(self, data):
        """ DELETE API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def edit_application_comment(self, data):
        """ PUT API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def like_an_application(self, data):
        """ POST API_PATH/[APP_ID]/likes """
        return defaultMethodResponse

    def get_application_likes(self, data):
        """ GET API_PATH/[APP_ID]/likes """
        return defaultMethodResponse

    def unlike_application(self, data):
        """ DELETE API_PATH/[APP_ID]/likes """
        return defaultMethodResponse

    def dislike_application(self, data):
        """ POST API_PATH/[APP_ID]/dislikes """
        return defaultMethodResponse

    def get_application_dislikes(self, data):
        """ GET API_PATH/[APP_ID]/dislikes """
        return defaultMethodResponse

    def delete_application_dislikes(self, data):
        """ DELETE API_PATH/[APP_ID]/dislikes """
        return defaultMethodResponse


    #   endregion Connections

    #   endregion Application Object

    #   endregion Profiles API