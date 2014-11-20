__author__ = 'mpetyx'

from tastypie import fields

from .models import OpeniFolder
from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.resources import BaseFileResource
from OPENiapp.APIS.OPENIResource import OpeniResource


class FolderResource(OpeniResource):
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
