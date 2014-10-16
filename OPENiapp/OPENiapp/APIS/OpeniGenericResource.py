__author__ = 'mpetyx'

from OPENiapp.APIS.Context.BaseResource import ContextAwareResource

from django.http import HttpResponse
from django.shortcuts import render
import ast
import logging

from allauth.socialaccount.models import SocialToken

from django.contrib.auth.models import User

from OPENiapp.Providers.generic import execution

from django.conf.urls import url
from tastypie.utils import trailing_slash
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

from tastypie import fields
from OPENiapp.APIS.Context.Resources import ContextResource

class GenericResource(ContextAwareResource):
    context = fields.ForeignKey(ContextResource, 'context', null=True, blank=True) # ,related_name='Context'
    def applications_asked(self, bundle):

        return 1

    def http_headers_in_request(self, bundle):

        return 1

    def request_method(self, bundle):

        return bundle.request.method()

    def get_list(self, request, **kwargs):
        """
        Returns a serialized list of resources.

        Calls ``obj_get_list`` to provide the data, then handles that result
        set and serializes it.

        Should return a HttpResponse (200 OK).
        """
        cbs = ["OPENi"]
        params = ""
        id = ""
        connection = ""
        if 'id' in kwargs:
            id = kwargs['id']
        if 'connection' in kwargs:
            connection = kwargs['connection']
        try:
            user = request.GET.get("user")
            u = User.objects.filter(username=user)
            cbs = ast.literal_eval(request.GET.get("cbs"))
            id = ast.literal_eval(request.GET.get("id"))
            params = ast.literal_eval(request.GET.get("params"))

            #apps = ast.literal_eval(request.GET.get("apps"))
            #method = request.GET.get("method")
            #data = ast.literal_eval(request.GET.get("data"))
        except:
            logging.info("no cbs is being asked")

        request_method = request.META['REQUEST_METHOD'].lower()
        path = request.path

        pathArray = path.split('/')
        version = pathArray[1]
        object = pathArray[2].lower()

        method = request_method + '_' + object
        if (id != ""):
            # method += '_' + str(id)
            if (connection != ""):
                method += '_' + connection
        else:
            if (object == 'status'):
                method += 'e'
            if (object != 'rsvp'):
                method += 's'

        executable = execution(u, cbs, method, id, params)
        result = executable.make_all_connections()
        return self.create_response(request, result)

        #append_to_method = "_"
        #connections = []
        #if (len(pathArray) > 3):
        #    connections = pathArray[3:]
        #for part in connections:
        #    append_to_method += part

        #if (len(pathArray) > 3):
        #    if (pathArray[3] != ""):
        #        id = pathArray[3]
        #if (len(pathArray) > 4):
        #    connection = pathArray[4]

        # if request_method:
        #     method = request_method + '_' + object
        #     if len(connection)>1:
        #        method += "_" + connection
        #
        #     executable = execution(u, cbs, method, id, params)
        #     result = executable.make_all_connections()
        #     return self.create_response(request, result)

        #if (user and apps and method and data):
        #    executable = execution(u, apps, method, data)
            
        #    result = executable.make_all_connections()
        #    return self.create_response(request, result)
        
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
        return self.create_response(request, to_be_serialized)

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<id>\S+)/(?P<connection>\S+)%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_list'), name="connections"),
            url(r"^(?P<resource_name>%s)/(?P<id>\S+)%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_list'), name="id")
        ]

class GenericMeta:
    list_allowed_methods = ['get', 'post']
    detail_allowed_methods = ['get', 'post', 'put', 'delete']
    authentication = Authentication()
    authorization = Authorization()
    # filtering = {
    #     'slug': ALL,
    #     'user': ALL_WITH_RELATIONS,
    #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
    # }


    extra_actions = [

        {
            "name": "generic",
            "http_method": "GET",
            "resource_type": "list",
            "description": "Apply Method",
            "fields": {
                "user": {
                    "type": "string",
                    "required": True,
                    "description": "The user required for this action"
                },
                "apps": {
                    "type": "string",
                    "required": True,
                    "description": "The CBS along with the App we want to do a request to"
                },
                "method": {
                    "type": "string",
                    "required": True,
                    "description": "Method needed"
                },
                "data": {
                    "type": "String",
                    "required": True,
                    "description": "The required data",
            #         'allowableValues': {
            #     'valueType' : "LIST",
            #     'values': ["yo"]
            #
            # }
          #           'allowableValues': {
          #       'valueType' : "LIST",
          #       'values': [
          #   "placed",
          #   " approved",
          #   " delivered"
          # ]
          #
          #   },
                },
            }
        },

        # {
        #     "name": "comments",
        #     "http_method": "GET",
        #     "resource_type": "list",
        #     "description": "comments from CBS",
        #     "fields": {
        #         "cbs": {
        #             "type": "string",
        #             "required": True,
        #             "description": "list of selected CBS"
        #         }
        #     }
        # },
        #
        # {
        #     "name": "likes",
        #     "http_method": "GET",
        #     "resource_type": "list",
        #     "description": "likes from CBS",
        #     "fields": {
        #         "cbs": {
        #             "type": "string",
        #             "required": True,
        #             "description": "list of selected CBS"
        #         }
        #     }
        # },
        #
        # {
        #     "name": "dislikes",
        #     "http_method": "GET",
        #     "resource_type": "list",
        #     "description": "dislikes from CBS",
        #     "fields": {
        #         "cbs": {
        #             "type": "string",
        #             "required": True,
        #             "description": "list of selected CBS"
        #         }
        #     }
        # }
    ]