__author__ = 'mpetyx'

from tastypie.resources import ModelResource
from OPENiapp.APIS.models import *
from tastypie.authorization import Authorization
from OPENiapp.APIS.models import TagsModel, AddressModel, PersonModel, FromModel, TimeModel, DurationModel, \
    LocationModel, OrganizationModel, BaseFileModel, ApplicationModel, SizeModel, PlaceModel, ServiceModel, ProductModel

class PersonModelResource(ModelResource):

    class Meta:
        queryset = PersonModel.objects.all()
        list_allowed_methods = ['get','post']
        resource_name = "Person"

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


class AddressResource(ModelResource):
    class Meta:
        queryset = AddressModel.objects.all()
        resource_name = "Address"
        authorization = Authorization()

class TagsResource(ModelResource):
    class Meta:
        queryset = TagsModel.objects.all()
        resource_name = "BaseTags"
        authorization = Authorization()

class BaseSizeResource(ModelResource):
    class Meta:
        queryset = SizeModel.objects.all()
        resource_name = "Size"
        authorization = Authorization()

class BaseApplicationResource(ModelResource):
    class Meta:
        queryset = ApplicationModel.objects.all()
        resource_name = "Application"
        authorization = Authorization()

class BaseFileResource(ModelResource):
    class Meta:
        queryset = BaseFileModel.objects.all()
        resource_name = "BaseFile"
        authorization = Authorization()

class BaseOrganizationResource(ModelResource):
    class Meta:
        queryset = OrganizationModel.objects.all()
        resource_name = "Application"
        authorization = Authorization()

class BasePlaceResource(ModelResource):
    class Meta:
        queryset = PlaceModel.objects.all()
        resource_name = "BasePlace"
        authorization = Authorization()

class BaseProductResource(ModelResource):
    class Meta:
        queryset = ProductModel.objects.all()
        resource_name = "BaseProduct"
        authorization = Authorization()

class BaseServiceResource(ModelResource):
    class Meta:
        queryset = ServiceModel.objects.all()
        resource_name = "BaseService"
        authorization = Authorization()

