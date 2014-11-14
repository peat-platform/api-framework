__author__ = 'mpetyx'

from tastypie.resources import ModelResource
from OPENiapp.APIS.models import *
from tastypie.authorization import Authorization


class PersonModelResource(ModelResource):

    class Meta:
        queryset = PersonModel.objects.all()
        list_allowed_methods = ['get','post']
        resource_name = "PersonModel"

class FromResource(ModelResource):

    class Meta:
        queryset = FromModel.objects.all()
        resource_name = "From"

class TimeResource(ModelResource):

    class Meta:
        queryset = TimeModel.objects.all()
        resource_name = "Time"

class DurationResource(ModelResource):
    class Meta:
        queryset = DurationModel.objects.all()
        resource_name = "Duration"
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

class LocationResource(ModelResource):
    class Meta:
        queryset = LocationModel.objects.all()
        resource_name = "Location"
        authorization = Authorization()


# class OpeniNoteResource(ModelResource):
#     class Meta:
#         queryset = OpeninoteModel.objects.all()
#         resource_name = "Note"
