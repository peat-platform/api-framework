__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniPlace

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class PlaceResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniPlace.objects.all()
        resource_name = 'Place'
        authentication = Authentication()
        authorization = Authorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }

        extra_actions = [
            {
                "name": "",
                "http_method": "GET",
                "resource_type": "list", # view
                "summary": "Retrieve a list of Checkin Likes",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Google, Citygrid"
                    },
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
                }
            }
        ]
