__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniGame

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta


class GameResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniGame.objects.all()
        resource_name = 'Game'

        extra_actions = [
            {
                "name": "scores",
                "http_method": "GET",
                "summary": "Retrieve the user scores for a profile from CBS",
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
                        "description": "Facebook"
                    },

                }
            },
            {
                "name": "scores",
                "http_method": "DELETE",
                "summary": "DELETE the user scores for a profile from CBS",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Current user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    },
                    "id":{
                        "type": "string",
                        "required": False,
                        "description": "Facebook"
                    }

                }
            }
        ]
