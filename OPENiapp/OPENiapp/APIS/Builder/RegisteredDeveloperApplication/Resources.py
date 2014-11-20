__author__ = 'mpetyx'

from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
# from OPENiapp.APIS.OPENiAuthentication import Authentication

from tastypie.authentication import ApiKeyAuthentication

from OPENiapp.models import RegisteredApplication
from OPENiapp.APIS.OPENIResource import OpeniResource


class RegisteredApplicationResource(OpeniResource):
    class Meta(GenericMeta):
        queryset = RegisteredApplication.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Registeredapplication'
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }