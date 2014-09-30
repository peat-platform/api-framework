from tastypie.authorization import DjangoAuthorization
from .models import OpeniCart

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class CartResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniCart.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Cart'
        authentication = Authentication()
        authorization = Authorization()