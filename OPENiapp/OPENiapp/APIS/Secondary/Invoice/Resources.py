from tastypie.authorization import DjangoAuthorization
from .models import OpeniInvoice

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class InvoiceResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniInvoice.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Invoice'
        authentication = Authentication()
        authorization = Authorization()