__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniNotebook

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication


class NotebookResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniNotebook.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Notebook'
        authentication = Authentication()
        authorization = Authorization()