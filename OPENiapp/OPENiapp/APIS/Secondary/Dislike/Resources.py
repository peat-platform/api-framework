from tastypie.authorization import DjangoAuthorization
from .models import OpeniDislike

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class DislikeResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniDislike.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Dislike'
        authentication = Authentication()
        authorization = Authorization()