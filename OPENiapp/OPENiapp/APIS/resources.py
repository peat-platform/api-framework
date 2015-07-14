__author__ = 'mpetyx'

# from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from OPENiapp.APIS.models import TagsModel, AddressModel, PersonModel, FromModel, TimeModel, DurationModel, \
    LocationModel, OrganizationModel, BaseFileModel, ApplicationModel, SizeModel, PlaceModel, ServiceModel, ProductModel
# from OPENIResource import OpeniResource
from OPENiapp.APIS.OPENIResource import OpeniResource
from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from tastypie import fields



class PersonModelResource(OpeniResource):
    class Meta:
        resource_name = "Person"
        object_class = PersonModel


class FromResource(OpeniResource):
    class Meta:
        resource_name = "From"
        object_class = FromModel


class TimeResource(OpeniResource):
    class Meta:
        resource_name = "Time"
        object_class = TimeModel


class DurationResource(OpeniResource):
    class Meta:
        resource_name = "Duration"
        object_class = DurationModel
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
        resource_name = "Location"
        object_class  = LocationModel


class AddressResource(OpeniResource):
    class Meta:
        resource_name = "Address"
        object_class = AddressModel


class TagsResource(OpeniResource):
    class Meta:
        resource_name = "BaseTag"
        object_class = TagsModel


class BaseSizeResource(OpeniResource):
    class Meta:
        resource_name = "Size"
        object_class = SizeModel


class BaseApplicationResource(OpeniResource):
    category = fields.CharField(attribute='category', null=True, blank=True)

    class Meta(GenericMeta):
        resource_name = "Application"
        object_class = ApplicationModel


class BaseFileResource(OpeniResource):
    class Meta:
        resource_name = "BaseFile"
        object_class = BaseFileModel

class BaseOrganizationResource(OpeniResource):
    class Meta:
        resource_name = "Organization"
        object_class = OrganizationModel

class BasePlaceResource(OpeniResource):
    Location = fields.ForeignKey(LocationResource, 'Location', null=True, blank=True)

    class Meta:
        resource_name = "BasePlace"
        object_class = PlaceModel

class BaseProductResource(OpeniResource):
    class Meta:
        resource_name = "BaseProduct"
        object_class = ProductModel

class BaseServiceResource(OpeniResource):
    class Meta:
        resource_name = "BaseService"
        object_class = ServiceModel
