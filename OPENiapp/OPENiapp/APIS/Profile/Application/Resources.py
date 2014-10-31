__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniApplication

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class ApplicationResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniApplication.objects.all()
        resource_name = 'Application'


        extra_actions = [
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve the applications of the current user from CBS",
                "resource_type": "list",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, OPENi"
                    },

                }
            },
            {
                "name": "",
                "http_method": "POST",
                "summary": "",
                "resource_type": "list",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },

                }
            },
            {
                "name": "",
                "http_method": "DELETE",
                "summary": "",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },

                }
            },

            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve the applications of the current user from CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, OPENi"
                    },

                }
            },

            {
                "name": "",
                "http_method": "PUT",
                "summary": "Retrieve an application of the current user from CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, OPENi"
                    },
                    "auth_dialog_data_help_url":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "auth_dialog_headline":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "auth_dialog_perms_explanation":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "auth_referral_default_activity_privacy":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "auth_referral_enabled":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "auth_referral_extended_perms":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "auth_referral_friend_perms":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "auth_referral_user_perms":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "auth_referral_response_type":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "canvas_fluid_height":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "canvas_fluid_width":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "canvas_url":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "contact_email":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "deauth_callback_url":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "migrations":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "mobile_web_url":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "namespace":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "page_tab_default_name":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "page_tab_url":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "privacy_policy_url":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "restrictions":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "secure_canvas_url":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "secure_page_tab_url":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "server_ip_whitelist":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "social_discovery":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "terms_of_service_url":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "user_support_email":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "user_support_url":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "website_url":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },


                }
            },
            {
                "name": "likes",
                "http_method": "GET",
                "summary": "Get likes for an application",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },


                }
            },
            {
                "name": "comments",
                "http_method": "GET",
                "summary": "Get comments for an application",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },


                }
            },
            {
                "name": "dislikes",
                "http_method": "GET",
                "summary": "Get dislikes for an application",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },


                }
            },
            {
                "name": "likes",
                "http_method": "POST",
                "summary": "Like an application",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },


                }
            },
            {
                "name": "comments",
                "http_method": "POST",
                "summary": "Post comment for an application",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },


                }
            },
            {
                "name": "dislikes",
                "http_method": "POST",
                "summary": "Dislikes an application",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },


                }
            },
            {
                "name": "dislikes",
                "http_method": "DELETE",
                "summary": "Delete a dislike of an application",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },


                }
            },
            {
                "name": "likes",
                "http_method": "DELETE",
                "summary": "Delete a like of an application",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },


                }
            }
        ]
