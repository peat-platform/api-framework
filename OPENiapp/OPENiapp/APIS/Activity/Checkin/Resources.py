__author__ = 'mpetyx'


from .models import OpeniCheckin

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication


class CheckinResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniCheckin.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put', 'delete']
        resource_name = 'Checkin'
        authentication = Authentication()
        authorization = Authorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }

        extra_actions = [
            {
                "name": "likes",
                "http_method": "GET",
                "summary": "Retrieve a list of Checkin Likes",
                "fields": {}
            },
            {
                "name": "likes",
                "http_method": "POST",
                "summary": "Like a Checkin",
                "fields": {}
            },
            {
                "name": "comments",
                "http_method": "GET",
                "summary": "Retrieve a list of Checkin Comments",
                "fields": {}
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
