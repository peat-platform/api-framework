__author__ = 'mpetyx'

from .models import OpeniRoute

from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.OPENIResource import OpeniResource


class RouteResource(OpeniResource):
    class Meta(GenericMeta):
        object_class = OpeniRoute
        resource_name = 'Route'
        extra_actions = [
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

        ]
