__author__ = 'mpetyx'

from tastypie import fields

from .models import OpeniVideo
from OPENiapp.APIS.resources import BaseFileResource
from OPENiapp.APIS.resources import TagsResource, DurationResource
from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.OPENIResource import OpeniResource


class VideoResource(OpeniResource):
    Duration = fields.ForeignKey(DurationResource, 'Duration', null=True, blank=True)
    BaseTag = fields.ForeignKey(TagsResource, 'BaseTag', null=True, blank=True)
    BaseFile = fields.ForeignKey(BaseFileResource, 'BaseFile', null=True, blank=True)

    class Meta(GenericMeta):
        object_class = OpeniVideo
        resource_name = 'Video'

        extra_actions = [
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
                        "description": "Facebook, OPENi"
                    }

                }
            },
            {
                "name": "",
                "http_method": "DELETE",
                "summary": "Delete a user Video from CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, OPENi"
                    }

                }
            },
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve all user Videos from CBS",
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
                        "description": "Facebook, OPENi"
                    }

                }
            },
            {
                "name": "",
                "http_method": "POST",
                "summary": "Post a new Video on CBS",
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
                        "description": "Facebook, OPENi"
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
                "summary": "Post a new comment on target Video on CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook, OPENi"
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
                    "attachment_source": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "message": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    }

                }
            },
            {
                "name": "Comments",
                "http_method": "GET",
                "summary": "GET comments from Video on CBS",
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
                    }

                }
            },
            {
                "name": "Likes",
                "http_method": "POST",
                "summary": "Post a new like on target Video on CBS",
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
                    }

                }
            },
            {
                "name": "Likes",
                "http_method": "GET",
                "summary": "GET likes from Video on CBS",
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
                    }

                }
            },
            {
                "name": "Likes",
                "http_method": "DELETE",
                "summary": "Delete likes from Video on CBS",
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
                    }

                }
            }
        ]
