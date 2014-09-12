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
    context = fields.ForeignKey(ContextResource, 'Context',related_name='Context', null=True, blank=True)
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
        try:
            user = request.GET.get("user")
            u = User.objects.filter(username=user)

            apps = ast.literal_eval(request.GET.get("apps"))
            method = request.GET.get("method")
            data = ast.literal_eval(request.GET.get("data"))
        except:
            logging.info("no cbs is being asked")

        if (user and apps and method and data):
            #executable = execution(u, [{"cbs": "instagram", "app_name": "OPENi"}], "get_a_photo", {"media_id": "628147512937366504_917877895"})
            #executable = execution(u, [{"cbs": "instagram", "app_name": "OPENi"}], "get_all_photos_for_account", {"account_id": "917877895"})
            #executable = execution(u, [{"cbs": "foursquare", "app_name": "OPENi"}], "get_user", {})
            #executable = execution(u, [{"cbs": "facebook", "app_name": "OPENi"}], "get_an_event", {"event_id": "577733618968497"})
            #executable = execution(u, [{"cbs": "facebook", "app_name": "OPENi"}], "get_all_events_for_account", {"account_id": "1266965453"})
            #executable = execution(u, [{"cbs": "facebook", "app_name": "OPENi"}], "post_event_to_account", {"account_id": "me", 'name': 'kati', 'start_time': '2014-01-24T23:30:00+0200'})
            #executable = execution(u, [{"cbs": "facebook", "app_name": "OPENi"}], "edit_an_event", {"event_id": "235785719933823", 'name': 'kati_allo', 'start_time': '2014-01-24T23:30:00+0200'})
            #executable = execution(u, [{"cbs": "facebook", "app_name": "OPENi"}], "delete_an_event", {"event_id": "235785719933823"})
            executable = execution(u, apps, method, data)
            
            result = executable.make_all_connections()
            return self.create_response(request, result)
        
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
            url(r"^(?P<resource_name>%s)/generic%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_list'), name="generic"),
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
                    "type": "string",
                    "required": True,
                    "description": "The required data"
                },
            }
        },

        {
            "name": "comments",
            "http_method": "GET",
            "resource_type": "list",
            "description": "comments from CBS",
            "fields": {
                "cbs": {
                    "type": "string",
                    "required": True,
                    "description": "list of selected CBS"
                }
            }
        },

        {
            "name": "likes",
            "http_method": "GET",
            "resource_type": "list",
            "description": "likes from CBS",
            "fields": {
                "cbs": {
                    "type": "string",
                    "required": True,
                    "description": "list of selected CBS"
                }
            }
        },

        {
            "name": "dislikes",
            "http_method": "GET",
            "resource_type": "list",
            "description": "dislikes from CBS",
            "fields": {
                "cbs": {
                    "type": "string",
                    "required": True,
                    "description": "list of selected CBS"
                }
            }
        }
    ]