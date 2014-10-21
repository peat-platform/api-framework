__author__ = 'mpetyx'


from .models import OpeniCheckin

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication


class CheckinResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniCheckin.objects.all()
        resource_name = 'Checkin'
        authentication = Authentication()
        authorization = Authorization()
        list_allowed_methods = []
        detail_allowed_methods = []
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }

        extra_actions = [
            {
                "name": "",
                "http_method": "POST",
                "summary": "Create a new openi checkin",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "The CBS you want to make a call to"
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
                "http_method": "PUT",
                "summary": "Update an existing OPENi checkin",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "The CBS you want to make a call to"
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
                "http_method": "DELETE",
                "summary": "Delete an existing OPENi checkin",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "The CBS you want to make a call to"
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
                "summary": "Retrieve a single OPENi,Facebook or Foursquare checkin by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "The CBS you want to make a call to"
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
                "summary": "Retrieve a list of OPENi,Facebook and Foursquare checkins",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "The CBS you want to make a call to"
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
                "name": "likes",
                "http_method": "GET",
                "summary": "Retrieve a list of Checkin Likes",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "The CBS you want to make a call to"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
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
                        "description": "The CBS you want to make a call to"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
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
                        "description": "The CBS you want to make a call to"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
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
                        "description": "Text of the Comment, (Facebook: message, Twitter: status)"
                    },
                    "attachment_id": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook: Attachment ID"
                    },
                    "attachment_url": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook: Attachment url"
                    },
                    "source": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook: Source"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "The CBS you want to make a call to"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                }
            }
        ]
