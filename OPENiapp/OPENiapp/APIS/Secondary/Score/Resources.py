from tastypie.authorization import DjangoAuthorization
from .models import OpeniScore

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class ScoreResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniScore.objects.all()
        resource_name = 'Score'

        extra_actions = [
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve the scores of the current user from CBS",
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
            }
        ]
