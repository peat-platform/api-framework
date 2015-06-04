__author__ = 'mpetyx'

# from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from OPENiapp.APIS.models import TagsModel, AddressModel, PersonModel, FromModel, TimeModel, DurationModel, \
    LocationModel, OrganizationModel, BaseFileModel, ApplicationModel, SizeModel, PlaceModel, ServiceModel, ProductModel
# from OPENIResource import OpeniResource
from OPENiapp.APIS.OPENIResource import OpeniResource



class PersonModelResource(OpeniResource):
    class Meta:
        queryset = PersonModel.objects.all()
        list_allowed_methods = ['get', 'post']
        resource_name = "Person"
        authorization = Authorization()


class FromResource(OpeniResource):
    class Meta:
        queryset = FromModel.objects.all()
        resource_name = "From"
        authorization = Authorization()


class TimeResource(OpeniResource):
    class Meta:
        queryset = TimeModel.objects.all()
        resource_name = "Time"
        authorization = Authorization()


class DurationResource(OpeniResource):
    class Meta:
        queryset = DurationModel.objects.all()
        resource_name = "Duration"
        authorization = Authorization()
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


class LocationResource(OpeniResource):
    class Meta:
        queryset = LocationModel.objects.all()
        resource_name = "Location"
        authorization = Authorization()


class AddressResource(OpeniResource):
    class Meta:
        queryset = AddressModel.objects.all()
        resource_name = "Address"
        authorization = Authorization()


class TagsResource(OpeniResource):
    class Meta:
        queryset = TagsModel.objects.all()
        resource_name = "BaseTags"
        authorization = Authorization()


class BaseSizeResource(OpeniResource):
    class Meta:
        queryset = SizeModel.objects.all()
        resource_name = "Size"
        authorization = Authorization()


class BaseApplicationResource(OpeniResource):
    class Meta:
        queryset = ApplicationModel.objects.all()
        resource_name = "Application"
        authorization = Authorization()


class BaseFileResource(OpeniResource):
    class Meta:
        queryset = BaseFileModel.objects.all()
        resource_name = "BaseFile"
        authorization = Authorization()


class BaseOrganizationResource(OpeniResource):
    class Meta:
        queryset = OrganizationModel.objects.all()
        resource_name = "Application"
        authorization = Authorization()


class BasePlaceResource(OpeniResource):
    class Meta:
        queryset = PlaceModel.objects.all()
        resource_name = "BasePlace"
        authorization = Authorization()


class BaseProductResource(OpeniResource):
    class Meta:
        queryset = ProductModel.objects.all()
        resource_name = "BaseProduct"
        authorization = Authorization()


class BaseServiceResource(OpeniResource):
    class Meta:
        queryset = ServiceModel.objects.all()
        resource_name = "BaseService"
        authorization = Authorization()

