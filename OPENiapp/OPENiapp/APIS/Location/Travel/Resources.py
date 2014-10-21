__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniTravel

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class TravelResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniTravel.objects.all()
        resource_name = 'Travel'