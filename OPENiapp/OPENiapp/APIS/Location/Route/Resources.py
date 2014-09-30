__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniRoute

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class RouteResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniRoute.objects.all()
        resource_name = 'Route'
