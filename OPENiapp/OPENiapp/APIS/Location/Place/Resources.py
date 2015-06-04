__author__ = 'mpetyx'

from tastypie import fields

from .models import OpeniPlace
from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.resources import BasePlaceResource
from OPENiapp.APIS.OPENIResource import OpeniResource


class PlaceResource(OpeniResource):
    BasePlace = fields.ForeignKey(BasePlaceResource, 'BasePlace', null=True, blank=True)

    class Meta(GenericMeta):
        queryset = OpeniPlace.objects.all()
        resource_name = 'Place'

        extra_actions = [
            {
                "name": "",
                "http_method": "GET",
                #"resource_type": "list", # view
                "summary": "Retrieve a list of Places over CBS",
                "nickname": "Sample Naming",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Google, Citygrid"
                    }
                },

            },


            {
                "name": "",
                "http_method": "POST",
                "summary": "Create a new Place on CBS",
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
                        "description": "Google, Citygrid"
                    },
                    "name": {
                        "type": "string",
                        "required": False,
                        "description": "Google"
                    },
                    "lat_lng": {
                        "type": "string",
                        "required": False,
                        "description": "Google"
                    },
                    "accuracy": {
                        "type": "string",
                        "required": False,
                        "description": "Google"
                    },
                    "types": {
                        "type": "string",
                        "required": False,
                        "description": "Google"
                    },
                    "language": {
                        "type": "string",
                        "required": False,
                        "description": "Google"
                    },
                }
            },
            {
                "name": "",
                "http_method": "PUT",
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
                        "description": "Google, OPENi"
                    },

                }
            },


        ]
