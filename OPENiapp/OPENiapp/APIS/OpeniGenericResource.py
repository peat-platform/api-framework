__author__ = 'mpetyx'

from django.conf.urls import url
from tastypie.utils import trailing_slash
from tastypie import fields

from OPENiapp.APIS.Context.BaseResource import ContextAwareResource
from OPENiapp.APIS.OPENiAuthentication import Authentication
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.Context.Resources import ContextResource
from tastypie.serializers import Serializer
# from OPENiapp.APIS.resources import FromResource


class GenericResource(ContextAwareResource):
    context = fields.ForeignKey(ContextResource, 'context', null=True, blank=True) # ,related_name='Context'
    id = fields.CharField('id',null=True,blank=True)
    # From = fields.ForeignKey(FromResource, 'From', null=True, blank=True) # ,related_name='Context'
    # Time = fields.ForeignKey(TimeResource, 'Time', null=True, blank=True) # ,related_name='Context'

    def request_method(self, bundle):
        return bundle.request.method()

    def dehydrate(self, bundle):
        bundle.data['service'] = "OPENi Cloudlet"
        return bundle

    def get_resource_uri(self, bundle_or_obj=None, url_name='api_dispatch_list'):
        import json
        # print json.dumps(bundle_or_obj.data['url'])

        try:
            if "get" in bundle_or_obj.request.method.lower():
                #id = bundle_or_obj.data['url'].replace("https://demo2.openi-ict.eu/api/v1/objects/","")
                id = bundle_or_obj.data['url'].replace("https://localhost/api/v1/objects/","")
                id = id.split("/")[1]
                return "/v.04/"+self.Meta.resource_name+"/"+id
            else:
                return "Empty"
        except:
            return "/v.04/"+self.Meta.resource_name+"/"



    def get_list(self, request, **kwargs):
        cbs_data = self.cbs_handling(request=request, **kwargs)

        # Default actions down here, for get_list (that is if there is no fb or other CBS request!
        base_bundle    = self.build_bundle(request=request)
        objects        = self.obj_get_list(bundle=base_bundle, **self.remove_api_resource_names(kwargs))
        sorted_objects = self.apply_sorting(objects, options=request.GET)

        paginator = self._meta.paginator_class(request.GET, sorted_objects, #resource_uri=self.get_resource_uri(),
                                               limit=self._meta.limit, max_limit=self._meta.max_limit,
                                               collection_name=self._meta.collection_name)
        to_be_serialized = paginator.page()

        # Dehydrate the bundles in preparation for serialization.
        bundles = []

        for obj in to_be_serialized[self._meta.collection_name]:
            bundle = self.build_bundle(obj=obj, request=request)
            bundles.append(self.full_dehydrate(bundle, for_list=True))

        to_be_serialized[self._meta.collection_name] = bundles
        to_be_serialized = self.alter_list_data_to_serialize(request, to_be_serialized)
        #cbs_data.append(to_be_serialized)
        resp = {"cbs" : cbs_data, "cloudlet":to_be_serialized}

        print resp

        return self.create_response(request, resp)

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<id>\S+)/(?P<connection>\S+)%s$" % (
            self._meta.resource_name, trailing_slash()), self.wrap_view('get_list'), name="connections"),
            url(r"^(?P<resource_name>%s)/(?P<id>\S+)%s$" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_list'), name="id")
        ]


class GenericMeta:
    always_return_data = True
    list_allowed_methods = ['get', 'post','put','delete']
    detail_allowed_methods = ['get', 'post', 'put', 'delete']
    authentication = Authentication()
    authorization = Authorization()
    # excludes = ['id']
    # include_resource_uri = False

    # filtering = {
    #     'id': ['exact']
    # }

    # class OpeniResource(CloudletResource):
    #
    #     def __init__(self):
    #         pass