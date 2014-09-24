from tastypie.authorization import DjangoAuthorization
from .models import OpeniComment

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class CommentResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniComment.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Comment'
        authentication = Authentication()
        authorization = Authorization()