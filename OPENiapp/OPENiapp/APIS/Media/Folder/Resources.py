__author__ = 'mpetyx'

from tastypie.authorization import DjangoAuthorization
from .models import OpeniFolder

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class FolderResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniFolder.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Folder'
