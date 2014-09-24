from tastypie.authorization import DjangoAuthorization
from .models import OpeniRSVP

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class RSVPResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniRSVP.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'RSVP'
        authentication = Authentication()
        authorization = Authorization()