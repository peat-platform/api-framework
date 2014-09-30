from tastypie.authorization import DjangoAuthorization
from .models import OpeniLike

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class LikeResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniLike.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Like'
        authentication = Authentication()
        authorization = Authorization()