__author__ = 'mpetyx'

from tastypie import fields

from .models import OpeniAccount
from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.resources import PersonModelResource
from OPENiapp.APIS.OPENIResource import OpeniResource


class AccountResource(OpeniResource):
    Person = fields.ForeignKey(PersonModelResource, 'Person', null=True, blank=True)

    class Meta(GenericMeta):
        queryset = OpeniAccount.objects.all()
        resource_name = 'Account'

        extra_actions = [
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve the user profile from CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Foursquare, Google"
                    },

                }
            },
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve the user profile from CBS",
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
                        "description": "Facebook, Foursquare, Google"
                    },

                }
            },
            {
                "name": "",
                "http_method": "DELETE",
                "summary": "Delete the user profile from CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Foursquare, Google"
                    },

                }
            }
        ]
