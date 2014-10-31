__author__ = 'mpetyx'

from tastypie.authorization import DjangoAuthorization
from .models import OpeniVideo

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class VideoResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniVideo.objects.all()
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
