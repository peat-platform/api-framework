__author__ = 'mpetyx'

from OPENiapp.APIS.OpeniGenericResource import GenericResource
from tastypie.bundle import Bundle
import json
import re
import logging

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
    def cloudlet_client(self):
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
        host = "https://193.1.188.41"
        auth_token = request.META['HTTP_AUTHORIZATION']
        results = []

        self.cloudlet_client()
        resp = self.client.get_objects_by_type(host=host, auth_token=auth_token, type=self.Meta.resource_name)
        print resp
        data = resp.json()

        try:
            for temp in data['result']:
                result = temp["@data"]
                logging.error(type(result))
                Time = {
                    "created_time": "1-1-1111",
              "deleted_time": "string",
              "id": "integer",
              "edited_time": "string",
                "resource_uri": "string"
                }
                result["Time"] = CloudletObject(Time) #temp["_date_created"]
                result['object_type'] = str(self.Meta.resource_name)
                result['url'] = temp["@location"]
                results.append(CloudletObject(initial=result))
        except:
            results = []

        return results


    def obj_get_list(self, bundle, **kwargs):
        # Filtering disabled for brevity...

        matchObjectId = re.search(r'0[a-f,0-9]{7}-[a-f,0-9]{4}-4[a-f,0-9]{3}-[a-f,0-9]{4}-[a-f,0-9]{12}',
                                  bundle.request.path, re.M | re.I)

        if matchObjectId:
            return self.obj_get(bundle, **kwargs)
        else:
            return self.get_object_list(bundle.request)


    def obj_get(self, bundle, **kwargs):

        host = "https://" + bundle.request.META['HTTP_HOST']
        host = "https://193.1.188.41"
        auth_token = bundle.request.META['HTTP_AUTHORIZATION']
        id = kwargs['id']


        # TODO i could filter here from the obj_get_list
        self.cloudlet_client()
        cloudletObj = self.client.get_object_by_id(host=host, auth_token=auth_token, id=id)

        temp =  json.loads(cloudletObj['body'])

        result = temp["@data"]
        Time = {
                "created_time": "1-1-1111",
          "deleted_time": "string",
          "id": "integer",
          "edited_time": "string",
            "resource_uri": "string"
            }
        result["Time"] = CloudletObject(Time) #temp["_date_created"]
        result['object_type'] = str(self.Meta.resource_name)
        result['url'] = temp["@location"]

        return [CloudletObject(initial=result)]


    def obj_create(self, bundle, **kwargs):

        #bundle       = self.full_hydrate(bundle)

        host = "https://" + bundle.request.META['HTTP_HOST']
        host = "https://193.1.188.41"
        auth_token = bundle.request.META['HTTP_AUTHORIZATION']
        bundle.obj = CloudletObject(initial=kwargs)

        self.cloudlet_client()
        current_type = self.client.getTypeId(typeId=self.Meta.resource_name)

        to_be_created = {
            "@openi_type": current_type,
            "@data": bundle.data
        }

        self.cloudlet_client()
        resp = self.client.post_object(host=host, auth_token=auth_token, object=to_be_created)
        print resp

        bundle.obj.url = resp['body']

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

        self.cloudlet_client()
        self.client.delete(id)


    def rollback(self, bundles):
        pass