from tastypie import fields

__author__ = 'mpetyx'

from .models import OpeniCheckin
from OPENiapp.APIS.Location.Place.Resources import PlaceResource
from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from cloudletClient.CloudletResource import CloudletResource
from OPENiapp.APIS.OPENIResource import OpeniResource


class CheckinResource(OpeniResource):
    Place = fields.ForeignKey(PlaceResource, 'Place', null=True, blank=True)

    class Meta(GenericMeta):
        queryset = OpeniCheckin.objects.all()
        resource_name = 'Checkin'

        extra_actions = [
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve a single cbs checkin by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Google"
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
                "http_method": "GET",
                "summary": "Retrieve a list of cbs checkins",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Foursquare"
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
                "name": "",
                "http_method": "POST",
                "summary": "Create a new **** checkin",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "pending"
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
                "name": "likes",
                "http_method": "GET",
                "summary": "Retrieve a list of Checkin Likes",
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
                "name": "likes",
                "http_method": "POST",
                "summary": "Like a Checkin",
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
                "name": "comments",
                "http_method": "GET",
                "summary": "Retrieve a list of Checkin Comments",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi, Facebook"
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
                "summary": "Delete a Checkin",
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
                "name": "comments",
                "http_method": "POST",
                "summary": "Create a new Checkin Comment",
                "fields": {
                    "title": {
                        "type": "string",
                        "required": False,
                        "description": "Title of the Comment"
                    },
                    "text": {
                        "type": "string",
                        "required": False,
                        "description": "Text of the Comment"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenticated user"
                    },

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
        ]
