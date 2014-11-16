__author__ = 'mpetyx'

from OPENiapp.APIS.OpeniGenericResource import GenericResource
from OPENiapp.models import Cloudlet
from django.contrib.auth.models import User
# from tastypie.resources import Resource, ModelResource
# from tastypie import fields
from tastypie.bundle import Bundle
import json
import re

from .client import CloudletClient

class CloudletObject(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}

        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data

    class _meta:
        pass


class CloudletResource(GenericResource):

    def __init__(self):
        self.client = CloudletClient()


    def detail_uri_kwargs(self, bundle_or_obj):

        print  bundle_or_obj

        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.uuid
        else:
            kwargs['pk'] = bundle_or_obj.uuid

        # Need to be removed
        # kwargs['pk'] = "omorfia"

        return kwargs


    def get_object_list(self, request):

        print "get all"

        host       = "https://" + request.META['HTTP_HOST']
        auth_token = request.META['HTTP_AUTHORIZATION']
        results    = []

        resp = self.client.get_objects_by_type(host=host, auth_token=auth_token, type=self.Meta.resource_name)
        data = json.loads(resp.text)

        for temp in data['result']:
            results.append(CloudletObject(initial=temp['@data']))

        print results

        return results


    def obj_get_list(self, bundle, **kwargs):
        # Filtering disabled for brevity...

        matchObjectId = re.search( r'0[a-f,0-9]{7}-[a-f,0-9]{4}-4[a-f,0-9]{3}-[a-f,0-9]{4}-[a-f,0-9]{12}', bundle.request.path, re.M|re.I)

        if matchObjectId:
            return self.obj_get(bundle, **kwargs)
        else:
            return self.get_object_list(bundle.request)


    def obj_get(self, bundle, **kwargs):

        print "get by id"
        print kwargs

        host       = "https://" + bundle.request.META['HTTP_HOST']
        auth_token = bundle.request.META['HTTP_AUTHORIZATION']
        id         = kwargs['id']


        # TODO i could filter here from the obj_get_list
        cloudletObj = self.client.get_object_by_id(host=host, auth_token=auth_token, id=id)

        print cloudletObj['body']
        print json.loads(cloudletObj['body'])['@data']

        return CloudletObject(initial=json.loads(cloudletObj['body'])['@data'])


    def obj_create(self, bundle, **kwargs):

        #bundle       = self.full_hydrate(bundle)

        host       = "https://" + bundle.request.META['HTTP_HOST']
        auth_token = bundle.request.META['HTTP_AUTHORIZATION']
        bundle.obj = CloudletObject(initial=kwargs)

        current_type = self.client.getTypeId(typeId=self.Meta.resource_name)

        to_be_created = {
            "@openi_type" : current_type,
            "@data"       : bundle.data
        }

        resp = self.client.post_object(host=host, auth_token=auth_token, object=to_be_created)

        print resp

        return bundle


    def obj_update(self, bundle, **kwargs):
        return self.obj_create(bundle, **kwargs)


    def obj_delete_list(self, bundle, **kwargs):
        bucket = self._bucket()

        for key in bucket.get_keys():
            obj = bucket.get(key)
            obj.delete()


    def obj_delete(self, bundle, **kwargs):

        id = kwargs['pk']

        self.client.delete(id)


    def rollback(self, bundles):
        pass