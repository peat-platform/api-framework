__author__ = 'mpetyx'

from OPENiapp.APIS.OpeniGenericResource import GenericResource
from OPENiapp.models import Cloudlet
from django.contrib.auth.models import User
# from tastypie.resources import Resource, ModelResource
# from tastypie import fields
from tastypie.bundle import Bundle

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

def search_cloudlet_types(type):

    return "t_7c13ee95f5c64b925424e4070083873e-699"


class CloudletResource(GenericResource):

    def cloudlet_client(self, server=None, username=None, password=None):

        self.client = CloudletClient("https://demo1.openi-ict.eu", "dev","1234")
        self.client.auth()

    def _client(self,bundle, username, password):
        current_user = User.objects.get(pk = bundle.request.user.id)
        owner = Cloudlet.objects.get()
        return CloudletClient(username=owner.username,password=owner.password)

    def _bucket(self):
        client = self._client()
        return client.bucket('messages')


    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.uuid
        else:
            kwargs['pk'] = bundle_or_obj.uuid

        # Need to be removed
        # kwargs['pk'] = "omorfia"

        return kwargs

    def get_object_list(self, request):
        # results = self._client.get_object_list()
        results = []

        # Bringing the results from Object list and serializing it into json objects based on schema
        temp = dict({'uuid':"michael",'title':2, 'description':4, 'icon':2, "id":1987})
        # Appending each one to the results

        # TODO remove when code is more stable
        self.cloudlet_client()
        self.client.change_server("https://demo2.openi-ict.eu")

        current_type = search_cloudlet_types(self.Meta.resource_name)

        for temp in self.client.get_object_by_type(type="t_7c13ee95f5c64b925424e4070083873e-699")['json response']['result']:
            results.append(CloudletObject(initial=temp['@data']))

        return results

    def obj_get_list(self, bundle, **kwargs):
        # Filtering disabled for brevity...
        return self.get_object_list(bundle.request)

    def obj_get(self, bundle, **kwargs):

        self.cloudlet_client()

        id = kwargs['pk']

        self.client.change_server("https://demo2.openi-ict.eu")

        # TODO i could filter here from the obj_get_list
        temp = self.client.get_object_by_id(id)['json response']['result']['@data']

        return CloudletObject(initial=temp)

    def obj_create(self, bundle, **kwargs):
        bundle.obj = CloudletObject(initial=kwargs)
        bundle = self.full_hydrate(bundle)
        print bundle.obj.to_dict()

        current_type = search_cloudlet_types(self.Meta.resource_name)

        to_be_created = {
        "@openi_type": current_type,
        "@data": bundle.obj.to_dict()
            }
        self.cloudlet_client()
        self.client.change_server("https://demo2.openi-ict.eu")

        self.client.post_object(to_be_created)

        # bucket = self._bucket()
        # new_message = bucket.new(bundle.obj.uuid, data=bundle.obj.to_dict())
        # new_message.store()
        return bundle

    def obj_update(self, bundle, **kwargs):
        return self.obj_create(bundle, **kwargs)

    def obj_delete_list(self, bundle, **kwargs):
        bucket = self._bucket()

        for key in bucket.get_keys():
            obj = bucket.get(key)
            obj.delete()

    def obj_delete(self, bundle, **kwargs):
        self.cloudlet_client()

        id = kwargs['pk']

        self.client.change_server("https://demo2.openi-ict.eu")
        self.client.delete(id)

    def rollback(self, bundles):
        pass