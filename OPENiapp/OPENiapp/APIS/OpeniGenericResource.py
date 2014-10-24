__author__ = 'mpetyx'

from OPENiapp.APIS.Context.BaseResource import ContextAwareResource

from django.conf.urls import url
from tastypie.utils import trailing_slash
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

from tastypie import fields
from OPENiapp.APIS.Context.Resources import ContextResource
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from OPENiapp.APIS.resources import *


class GenericResource(ContextAwareResource):
    context = fields.ForeignKey(ContextResource, 'context', null=True, blank=True) # ,related_name='Context'
    From = fields.ForeignKey(FromResource, 'From', null=True, blank=True) # ,related_name='Context'
    Time = fields.ForeignKey(TimeResource, 'Time', null=True, blank=True) # ,related_name='Context'

    def request_method(self, bundle):

        return bundle.request.method()


    def get_list(self, request, **kwargs):

        cbs_data = self.cbs_handling(request=request, **kwargs)
        
        # Default actions down here, for get_list (that is if there is no fb or other CBS request!
        base_bundle = self.build_bundle(request=request)
        objects = self.obj_get_list(bundle=base_bundle, **self.remove_api_resource_names(kwargs))
        sorted_objects = self.apply_sorting(objects, options=request.GET)

        paginator = self._meta.paginator_class(request.GET, sorted_objects, resource_uri=self.get_resource_uri(), limit=self._meta.limit, max_limit=self._meta.max_limit, collection_name=self._meta.collection_name)
        to_be_serialized = paginator.page()

        # Dehydrate the bundles in preparation for serialization.
        bundles = []

        for obj in to_be_serialized[self._meta.collection_name]:
            bundle = self.build_bundle(obj=obj, request=request)
            bundles.append(self.full_dehydrate(bundle, for_list=True))

        to_be_serialized[self._meta.collection_name] = bundles
        to_be_serialized = self.alter_list_data_to_serialize(request, to_be_serialized)
        cbs_data.append(to_be_serialized)
        return self.create_response(request, cbs_data)

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<id>\S+)/(?P<connection>\S+)%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_list'), name="connections"),
            url(r"^(?P<resource_name>%s)/(?P<id>\S+)%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_list'), name="id")
        ]

class GenericMeta:
    always_return_data = True
    list_allowed_methods = ['get', 'post']
    detail_allowed_methods = ['get', 'post', 'put', 'delete']
    authentication = Authentication()
    authorization = Authorization()
    #
    # filtering = {
    #         'id': ALL,
    #         'id': ALL_WITH_RELATIONS,
    #     }

    # extra_actions = [
    #
    #     {
    #         "name": "generic",
    #         "http_method": "GET",
    #         "resource_type": "list",
    #         "description": "Apply Method",
    #         "fields": {
    #             "user": {
    #                 "type": "string",
    #                 "required": True,
    #                 "description": "The user required for this action"
    #             },
    #             "apps": {
    #                 "type": "string",
    #                 "required": True,
    #                 "description": "The CBS along with the App we want to do a request to"
    #             },
    #             "method": {
    #                 "type": "string",
    #                 "required": True,
    #                 "description": "Method needed"
    #             },
    #             "data": {
    #                 "type": "String",
    #                 "required": True,
    #                 "description": "The required data",
    #         #         'allowableValues': {
    #         #     'valueType' : "LIST",
    #         #     'values': ["yo"]
    #         #
    #         # }
    #       #           'allowableValues': {
    #       #       'valueType' : "LIST",
    #       #       'values': [
    #       #   "placed",
    #       #   " approved",
    #       #   " delivered"
    #       # ]
    #       #
    #       #   },
    #             },
    #         }
    #     },
    #
    #
    # ]