__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniNote

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication


class NoteResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniNote.objects.all()
        resource_name = 'Note'
        extra_actions = [
            {
                "name": "comments",
                "http_method": "GET",
                "summary": "Retrieve comments for a single openi note by id",
                 "fields": {
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                },
            },
            {
                "name": "likes",
                "http_method": "GET",
                "summary": "Retrieve likes for a single openi note by id",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                },
            }
        ]