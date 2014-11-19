__author__ = 'mpetyx'

from tastypie.authorization import DjangoAuthorization
from .models import OpeniFolder
from tastypie import fields
from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication
from OPENiapp.APIS.resources import BaseFileResource

class FolderResource(GenericResource):
    BaseFile = fields.ForeignKey(BaseFileResource, 'BaseFile')
    class Meta(GenericMeta):
        queryset = OpeniFolder.objects.all()
        resource_name = 'Folder'

        extra_actions = [
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve a user folder from CBS",
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
                "name": "",
                "http_method": "POST",
                "summary": "Create a new folder on CBS",
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

            #   TODO  def post_folder_to_account(self, id, params):

        ]
