from tastypie.authorization import DjangoAuthorization
from .models import OpeniTag

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class TagResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniTag.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Tag'
        authentication = Authentication()
        authorization = Authorization()