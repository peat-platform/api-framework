__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniStatus

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class StatusResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniStatus.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Status'
        authentication = Authentication()
        authorization = Authorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }

        

    #def prepend_urls(self):
    #    return [
    #        url(r"^(?P<resource_name>%s)/(?P<pk>\d+)/status%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_property'), name="status")
    #        ]