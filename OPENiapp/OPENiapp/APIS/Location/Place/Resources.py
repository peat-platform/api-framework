__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniPlace

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication


class PlaceResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniPlace.objects.all()
        resource_name = 'Place'

        extra_actions = [
            {
                "name": "",
                "http_method": "GET",
                "resource_type": "list", # view
                "summary": "Retrieve a list of Places over CBS",
                "nickname":"Sample Naming",
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
                    "id":{
                        "description": "CityGrid",
                        "type": "string",
                        "required": False,

                    },
                    "id_type":{
                        "description": "CityGrid",
                        "type": "string",
                        "required": False,
                    },
                    "phone":{
                        "description": "CityGrid",
                        "type": "string",
                        "required": False,

                    },
                    "publisher":{
                        "description": "CityGrid",
                        "type": "string",
                        "required": False,

                    },
                    "customer_only":{
                        "description": "CityGrid",
                        "type": "string",
                        "required": False,

                    },
                    "all_results":{
                        "description": "CityGrid",
                        "type": "string",
                        "required": False,
                    },
                    "route":{
                        "description": "Google",
                        "type": "string",
                        "required": False,
                    },
                    "street_number":{
                        "description": "Google",
                        "type": "string",
                        "required": False,
                    },
                    "locality":{
                        "description": "Google",
                        "type": "string",
                        "required": False,
                    },
                    "country":{
                        "description": "Google",
                        "type": "string",
                        "required": False,
                    },
                    "postal_code":{
                        "description": "Google",
                        "type": "string",
                        "required": False,
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
