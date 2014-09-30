from tastypie.authorization import DjangoAuthorization
from .models import OpeniFavorite

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class FavoriteResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniFavorite.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Favorite'
        authentication = Authentication()
        authorization = Authorization()