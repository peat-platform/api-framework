from OPENiapp.APIS.Location.Place.Resources import PlaceResource
from OPENiapp.APIS.resources import DurationResource
from .models import OpeniEvent

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from cloudletClient.CloudletResource import CloudletResource

from tastypie import fields

class EventResource(CloudletResource):
    Place = fields.ForeignKey(PlaceResource, 'Place', null=True, blank=True)
    Duration = fields.ForeignKey(DurationResource, 'Duration', null=True, blank=True)
    class Meta(GenericMeta):
        queryset = OpeniEvent.objects.all()
        resource_name = 'Event'

        extra_actions = [
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve a single event by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Foursquare"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    }
                }
            },
            {
                "name": "",
                "http_method": "DELETE",
                "summary": "Delete an Event",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    }
                }
            },
            {
                "name": "",
                "http_method": "PUT",
                "summary": "Retrieve a list of cbs events",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    }
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
                "http_method": "GET",
                "summary": "Retrieve a list of cbs events",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    }
                },
                "resource_type": "list"
            },
            {
                "name": "rsvp",
                "http_method": "GET",
                "summary": "Retrieve rsvp for an event",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    }
                }
            },
            {
                "name": "rsvp",
                "http_method": "POST",
                "summary": "Create rsvp for an event",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    }
                }
            },


        ]