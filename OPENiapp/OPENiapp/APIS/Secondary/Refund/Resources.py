from tastypie.authorization import DjangoAuthorization
from .models import OpeniRefund

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class RefundResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniRefund.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Refund'
        authentication = Authentication()
        authorization = Authorization()