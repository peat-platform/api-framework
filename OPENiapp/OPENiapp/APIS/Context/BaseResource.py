from django.db import transaction
from tastypie import fields
from tastypie.exceptions import BadRequest
from tastypie.resources import ModelResource
from OPENiapp.APIS.Context.models import OpeniContext

import logging
import ast
from OPENiapp.Providers.generic import execution

from allauth.socialaccount.models import SocialToken

from django.contrib.auth.models import User


__author__ = 'amertis'
class ContextAwareResource(ModelResource):
    from OPENiapp.APIS.Context.Resources import ContextResource
    context = fields.ToOneField(ContextResource, 'context',full=True)

    # TODO remove this only to openigenericresource
    def cbs_handling(self, request,  **kwargs):
        cbs = ["OPENi"]
        params = ""
        id = ""
        connection = ""
        if 'id' in kwargs:
            id = kwargs['id']
        if 'connection' in kwargs:
            connection = kwargs['connection']

        user = request.GET.get("user")
        u = User.objects.filter(username=user)

        try:
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



    @transaction.atomic
    def obj_create(self, bundle, **kwargs):
        bundle = self.full_hydrate(bundle)

        ### EXTRA CODE
        self.cbs_handling(bundle.request,**kwargs)
        ### EXTRA CODE

        if bundle.obj.context is None:
            raise BadRequest("context attribute is not defined")
        bundle.obj.context.save()
        bundle.obj.context_id = bundle.obj.context.id
        bundle.obj.save()
        bundle.obj.context.objectid = bundle.obj.id
        # bundle.obj.context.save(update_fields=["objectid"])
        bundle.obj.context.save()
        return bundle
    @transaction.atomic
    def obj_update(self, bundle, **kwargs):

        ### EXTRA CODE
        self.cbs_handling(bundle.request,kwargs)
        ### EXTRA CODE

        if 'id' not in bundle.data:
            raise BadRequest("id property not found")
        bundle = self.full_hydrate(bundle)
        if bundle.obj.context.id is None:
            raise BadRequest("context id not found")
        bundle.obj.context.save()
        bundle.obj.save()
        return bundle
    # def obj_delete(self, bundle, **kwargs):
    #     return bundle
    @transaction.atomic
    def obj_delete(self, bundle, **kwargs):

        ### EXTRA CODE
        self.cbs_handling(bundle.request,kwargs)
        ### EXTRA CODE

        if 'pk' not in kwargs:
            raise BadRequest("no pk parameter found")
        try:
            pk = int(kwargs['pk'])
        except ValueError,e:
            raise BadRequest("invalid pk parameter")
        bundle = self.full_hydrate(bundle)
        type(bundle.obj).objects.filter(id=pk).delete()
        OpeniContext.objects.filter(objectid=pk).delete()
        return bundle