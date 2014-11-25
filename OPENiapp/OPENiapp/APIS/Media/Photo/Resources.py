__author__ = 'mpetyx'

from tastypie import fields

from .models import OpeniPhoto
from OPENiapp.APIS.resources import LocationResource
from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.resources import BaseFileResource
from OPENiapp.APIS.resources import TagsResource
from OPENiapp.APIS.OPENIResource import OpeniResource


class PhotoResource(OpeniResource):
    Location = fields.ForeignKey(LocationResource, 'Location', null=True, blank=True)
    BaseTag = fields.ForeignKey(TagsResource, 'BaseTag', null=True, blank=True)
    BaseFile = fields.ForeignKey(BaseFileResource, 'BaseFile', null=True, blank=True)

    class Meta(GenericMeta):
        object_class = OpeniPhoto
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
                        "description": "Registered and authenicated user"
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
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Instagram"
                    }

                }
            },
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve all user Photos from CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
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
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "source": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "url": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
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
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Flickr, Instagram"
                    },
                    "comment_text": {
                        "type": "string",
                        "required": False,
                        "description": "Flickr"
                    },
                    "attachment_id": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "attachment_url": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "message": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "url": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },

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
                        "description": "Registered and authenicated user"
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
                        "description": "Registered and authenicated user"
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
                        "description": "Registered and authenicated user"
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
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, Instagram"
                    }

                }
            }
        ]