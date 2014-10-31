__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniNotebook

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication


class NotebookResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniNotebook.objects.all()
        resource_name = 'Notebook'
        extra_actions = [
            {
                "name": "",
                "http_method": "DELETE",
                "summary": "Delete a Notebook",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "The CBS you want to make a call to"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    }
                }
            },
        ]