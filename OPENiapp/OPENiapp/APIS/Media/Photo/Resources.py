__author__ = 'mpetyx'

from .models import OpeniPhoto

from OPENiapp.Providers.Facebook.connector import provider as FBprovider
from OPENiapp.Providers.Twitter.connector import provider as TWprovider
from allauth.socialaccount.models import SocialToken

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

from tastypie.serializers import Serializer
from tastypie import fields
from OPENiapp.APIS.Context.Resources import ContextResource

class PhotoResource(GenericResource):

    class Meta(GenericMeta):
        queryset = OpeniPhoto.objects.all()
        resource_name = 'Photo'

        extra_actions = [
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve a user folder from CBS",
                "resource_type": "list",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },

                }
            },
            {
                "name": "",
                "http_method": "POST",
                "summary": "Create a new folder on CBS",
                "resource_type": "list",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },

                }
            }
        ]