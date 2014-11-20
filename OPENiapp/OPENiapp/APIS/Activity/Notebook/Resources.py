__author__ = 'mpetyx'

from tastypie import fields

from .models import OpeniNotebook
from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.Activity.Note.Resources import NoteResource
from OPENiapp.APIS.OPENIResource import OpeniResource


class NotebookResource(OpeniResource):
    Notes = fields.ForeignKey(NoteResource, 'Notes', null=True, blank=True)

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