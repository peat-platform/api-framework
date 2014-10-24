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
                "http_method": "PUT",
                "summary": "Retrieve an application of the current user from CBS",
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
