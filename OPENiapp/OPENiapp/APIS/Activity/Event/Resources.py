from tastypie.authorization import DjangoAuthorization
from OPENiapp.APIS.Location.Place.Resources import PlaceResource
from OPENiapp.APIS.resources import DurationResource
from .models import OpeniEvent

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication
from tastypie import fields

class EventResource(GenericResource):
    Place = fields.ForeignKey(PlaceResource, 'Place', null=True, blank=True)
    Duration = fields.ForeignKey(DurationResource, 'Duration', null=True, blank=True)
    class Meta(GenericMeta):
        queryset = OpeniEvent.objects.all()
        resource_name = 'Event'
        authentication = Authentication()
        authorization = Authorization()
        extra_actions = [
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve a single cbs status by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:Facebook,Twitter"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                }
            },

            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve a list of cbs events",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:Facebook,Twitter"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                },
                "resource_type": "list"
            },

            {
                "name": "",
                "http_method": "DELETE",
                "summary": "Retrieve a list of cbs events",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:Facebook,Twitter"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                },
            },

        ]