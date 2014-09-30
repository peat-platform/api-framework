from tastypie.authorization import DjangoAuthorization
from .models import OpeniReview

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class ReviewResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniReview.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Review'
        authentication = Authentication()
        authorization = Authorization()