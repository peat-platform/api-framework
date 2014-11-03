__author__ = 'mpetyx'

# We need a generic object to shove data in/get data from.
# Cloudlet generally just tosses around dictionaries, so we'll lightly
# wrap that.

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


class CloudletResource(GenericResource):

    def _client(self,bundle, username, password):
        current_user = User.objects.get(pk = bundle.request.user.id)
        owner = Cloudlet.objects.get()
        return CloudletClient(username=owner.username,password=owner.password)

    def _bucket(self):
        client = self._client()
        # Note that we're hard-coding the bucket to use. Fine for
        # example purposes, but you'll want to abstract this.
        return client.bucket('messages')

    # The following methods will need overriding regardless of your
    # data source.
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
        temp = dict({'uuid':"michael",'title':2, 'description':4, 'icon':2})
        # Appending each one to the results
        results.append(CloudletObject(initial=temp))

        return results

    def obj_get_list(self, bundle, **kwargs):
        # Filtering disabled for brevity...
        return self.get_object_list(bundle.request)

    def obj_get(self, bundle, **kwargs):
        bucket = self._bucket()
        message = bucket.get(kwargs['pk'])
        return CloudletObject(initial=message.get_data())

    def obj_create(self, bundle, **kwargs):
        bundle.obj = CloudletObject(initial=kwargs)
        bundle = self.full_hydrate(bundle)
        print bundle.obj.to_dict()
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
        bucket = self._bucket()
        obj = bucket.get(kwargs['pk'])
        obj.delete()

    def rollback(self, bundles):
        pass