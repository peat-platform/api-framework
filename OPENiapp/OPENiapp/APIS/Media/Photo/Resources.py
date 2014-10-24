__author__ = 'mpetyx'

from .models import OpeniPhoto

from OPENiapp.Providers.Facebook.connector import provider as FBprovider
from OPENiapp.Providers.Twitter.connector import provider as TWprovider
from allauth.socialaccount.models import SocialToken

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

from tastypie.serializers import Serializer
from tastypie import fields
from OPENiapp.APIS.Context.Resources import ContextResource

class PhotoResource(GenericResource):

    class Meta(GenericMeta):
        queryset = OpeniPhoto.objects.all()
        resource_name = 'Photo'

        extra_actions = [
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve all user Photos from CBS",
                "resource_type": "list",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Flickr, Foursquare, Instagram"
                    }

                }
            },
            {
                "name": "",
                "http_method": "DELETE",
                "summary": "Delete a user Photo from CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Flickr, Foursquare, Instagram"
                    }

                }
            },
            {
                "name": "Photos",
                "http_method": "GET",
                "summary": "Retrieve all user Photos from CBS",
                "resource_type": "list",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Flickr, Foursquare, Instagram"
                    }

                }
            },
            {
                "name": "",
                "http_method": "POST",
                "summary": "Post a new Photo on CBS",
                "resource_type": "list",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Instagram"
                    },

                }
            },
            {
                "name": "Comments",
                "http_method": "POST",
                "summary": "Post a new comment on target Photo on CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Flickr, Instagram"
                    }

                }
            },
            {
                "name": "Comments",
                "http_method": "GET",
                "summary": "GET comments from Photo on CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Flickr, Instagram"
                    }

                }
            },
            {
                "name": "Likes",
                "http_method": "POST",
                "summary": "Post a new like on target Photo on CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Instagram"
                    }

                }
            },
            {
                "name": "Likes",
                "http_method": "GET",
                "summary": "GET likes from Photo on CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Instagram"
                    }

                }
            },
            {
                "name": "Likes",
                "http_method": "DELETE",
                "summary": "Delete likes from Photo on CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Instagram"
                    }

                }
            }
        ]