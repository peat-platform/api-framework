from OPENiapp.Providers.base.productsServices import bcProductsServices
from OPENiapp.Providers.base.common import *

class fbProductsServices(bcProductsServices):
    """ This class is used to:
        1. Get a Facebook Application
        2. Get all Facebook Application for an account
        3. Edit a Facebook Application
    """
    #   region Profiles API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Products%20and%20Services%20API/
    
    #   region Application Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Application%20Mapping/
    
    def get_application(self, id):
        """ GET API_PATH/[APP_ID] """
        # /application_id (ie /10153665526210315)
        raw_data = self.connector.get('/' + id)
        
        names = ['id', 'object_type', 'service', 'resource_uri', 'from_id', 'from_object_type', 'from_resource_uri', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['application_title', 'application_description', 'application_version', 'application_icon', 'application_developer', 'adtype', 'adservices', 'adnetworks'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', 'from.object_type', 'from.url', 'from.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['name', 'description', 'version', 'icon_url', 'company', 'adtype', 'adservices', 'adnetwork'])

        alternatives = ['', 'application', 'facebook', '', 'Facebook User', '', '', '', '', '', '']
        alternatives.extend(['', '', '', '', '', '', '', ''])

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
            'meta': {
                'limit': self.check_if_exists(raw_data, 'limit', None),
                'next': self.check_if_exists(raw_data, 'paging.next', None),
                'offset': self.check_if_exists(raw_data, 'offset', 0),
                'previous': self.check_if_exists(raw_data, 'paging.previous', None),
                'total_count': self.check_if_exists(raw_data, 'total_count', 1)
            },
            'objects': [self.format_application_response(data)]
        }
        
        return response

    def get_applications(self):
        return self.get_all_applications_for_account('me')

    def get_all_applications_for_account(self, id):
        """ GET API_PATH/[ACCOUNT_ID]/applications """
        # Note: Facebook only returns applications where user is developer
        # /account_id/applications/developer (ie /675350314/applications/developer)
        raw_datas = self.connector.get('/' + id + '/applications/developer')
        
        names = ['id', 'object_type', 'service', 'resource_uri', 'from_id', 'from_object_type', 'from_resource_uri', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['application_title', 'application_description', 'application_version', 'application_icon', 'application_developer', 'adtype', 'adservices', 'adnetworks'])
        
        fields = ['id', 'object_type', 'service', 'link', 'from.id', 'from.object_type', 'from.url', 'from.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['name', 'description', 'version', 'icon_url', 'company', 'adtype', 'adservices', 'adnetwork'])

        alternatives = ['', 'application', 'facebook', '', 'Facebook User', '', '', '', '', '', '']
        alternatives.extend(['', '', '', '', '', '', '', ''])

        response = {
            'meta': {
                'limit': self.check_if_exists(raw_datas, 'limit', None),
                'next': self.check_if_exists(raw_datas, 'paging.next', None),
                'offset': self.check_if_exists(raw_datas, 'offset', 0),
                'previous': self.check_if_exists(raw_datas, 'paging.previous', None),
                'total_count': len(raw_datas['data'])
            },
            'objects': []
        }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['objects'].append(self.format_application_response(data))
                
        return response
    
    # To-Do: Fix this!
    def put_application(self, id, params):
        """ POST API_PATH/[APP_ID] """
        # /application_id (ie /10153665526210315)
        response = self.connector.post(
            '/' + id,
            app_domains = check_if_exists(params, 'app_domains', ''),
            auth_dialog_data_help_url = check_if_exists(params, 'auth_dialog_data_help_url', ''),
            auth_dialog_headline = check_if_exists(params, 'auth_dialog_headline', ''),
            auth_dialog_perms_explanation = check_if_exists(params, 'auth_dialog_perms_explanation', ''),
            auth_referral_default_activity_privacy = check_if_exists(params, 'auth_referral_default_activity_privacy', {}),
            auth_referral_enabled = check_if_exists(params, 'auth_referral_enabled', True),
            auth_referral_extended_perms = check_if_exists(params, 'auth_referral_extended_perms', ''),
            auth_referral_friend_perms = check_if_exists(params, 'auth_referral_friend_perms', ''),
            auth_referral_user_perms = check_if_exists(params, 'auth_referral_user_perms', ''),
            auth_referral_response_type = check_if_exists(params, 'auth_referral_response_type', {}),
            canvas_fluid_height = check_if_exists(params, 'canvas_fluid_height', true),
            canvas_fluid_width = check_if_exists(params, 'canvas_fluid_width', true),
            canvas_url = check_if_exists(params, 'canvas_url', ''),
            contact_email = check_if_exists(params, 'contact_email', ''),
            deauth_callback_url = check_if_exists(params, 'deauth_callback_url', ''),
            migrations = check_if_exists(params, 'migrations', {}),
            mobile_web_url = check_if_exists(params, 'mobile_web_url', ''),
            namespace = check_if_exists(params, 'namespace', ''),
            page_tab_default_name = check_if_exists(params, 'page_tab_default_name ', ''),
            page_tab_url = check_if_exists(params, 'page_tab_url', ''),
            privacy_policy_url = check_if_exists(params, 'privacy_policy_url', ''),
            restrictions = check_if_exists(params, 'restrictions', {}),
            secure_canvas_url = check_if_exists(params, 'secure_canvas_url ', ''),
            secure_page_tab_url = check_if_exists(params, 'secure_page_tab_url', ''),
            server_ip_whitelist = check_if_exists(params, 'server_ip_whitelist', ''),
            social_discovery = check_if_exists(params, 'social_discovery', True),
            terms_of_service_url = check_if_exists(params, 'terms_of_service_url', ''),
            user_support_email = check_if_exists(params, 'user_support_email', ''),
            user_support_url = check_if_exists(params, 'user_support_url', ''),
            website_url = check_if_exists(params, 'website_url', '')
            )
        return response
    
    #   region Connections


    #   endregion Connections

    #   endregion Application Object


    #   region Secondary Objects

    #   region Score Object

    def get_scores(self):
        return self.get_scores_from_account('me')

    def get_scores_from_account(self, id):
        """ GET API_PATH/{ACCOUNT_ID}/scores """
        # /account_id/scores (ie /675350314/scores)
        raw_datas = self.connector.get('/' + id + '/scores')
        
        names = ['id', 'object_type', 'service', 'resource_uri', 'from_id', 'from_object_type', 'from_resource_uri', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['value', 'target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'user.id', '', '', 'user.name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        fields.extend(['score', 'target_id'])

        alternatives = ['', 'score', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', ''])

        response = {
            'meta': {
                'limit': self.check_if_exists(raw_datas, 'limit', None),
                'next': self.check_if_exists(raw_datas, 'paging.next', None),
                'offset': self.check_if_exists(raw_datas, 'offset', 0),
                'previous': self.check_if_exists(raw_datas, 'paging.previous', None),
                'total_count': len(raw_datas['data'])
            },
            'objects': []
        }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['objects'].append(self.format_score_response(data))
                
        return response
    
    def get_game_scores(self, id):
        """ GET API_PATH/{GAME_ID}/scores """
        # /app_id/scores (ie /722334637784491/score)
        raw_datas = self.connector.get('/' + id + '/score')
        
        names = ['id', 'object_type', 'service', 'resource_uri', 'from_id', 'from_object_type', 'from_resource_uri', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['value', 'target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'user.id', '', '', 'user.name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        fields.extend(['score', 'target_id'])

        alternatives = ['', 'score', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', ''])

        response = {
            'meta': {
                'limit': self.check_if_exists(raw_datas, 'limit', None),
                'next': self.check_if_exists(raw_datas, 'paging.next', None),
                'offset': self.check_if_exists(raw_datas, 'offset', 0),
                'previous': self.check_if_exists(raw_datas, 'paging.previous', None),
                'total_count': len(raw_datas['data'])
            },
            'objects': []
        }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['objects'].append(self.format_score_response(data))
                
        return response

    def post_scores(self, params):
        return self.post_score_to_account('me', params)

    # Does not work due to FB's wrong documentation
    def post_score_to_account(self, id, params):
        """ POST API_PATH/{GAME_ID}/scores """
        # /account_id/scores (ie /675350314/scores)
        response = self.connector.post(
            '/' + id,
            score = check_if_exists(params, 'score', '')
            )
        return response

    def delete_game_scores(self, id):
        """ DELETE API_PATH/{GAME_ID}/scores """
        # /account_id/scores (ie /675350314/scores)
        response = self.connector.delete(
            '/' + id
            )
        return response

    #   endregion Score Objects

    #   endregion Secondary Objects

    #   endregion Products And Services API