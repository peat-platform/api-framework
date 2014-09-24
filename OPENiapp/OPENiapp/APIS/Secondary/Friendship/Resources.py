from tastypie.authorization import DjangoAuthorization
from .models import OpeniFriendship

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class FriendshipResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniFriendship.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Friendship'
        authentication = Authentication()
        authorization = Authorization()