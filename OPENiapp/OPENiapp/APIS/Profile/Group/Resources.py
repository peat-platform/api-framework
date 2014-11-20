# from .models import OpeniGroup
from django.contrib.auth.models import Group as OpeniGroup

from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication
from OPENiapp.APIS.OPENIResource import OpeniResource


class GroupResource(OpeniResource):
    class Meta(GenericMeta):
        queryset = OpeniGroup.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Group'
        authentication = Authentication()
        authorization = Authorization()
