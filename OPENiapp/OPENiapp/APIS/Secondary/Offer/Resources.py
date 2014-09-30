from tastypie.authorization import DjangoAuthorization
from .models import OpeniOffer

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class OfferResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniOffer.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Offer'
        authentication = Authentication()
        authorization = Authorization()