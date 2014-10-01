__author__ = 'mpetyx'

from tastypie.resources import ModelResource
from OPENiapp.APIS.models import *


class PersonModelResource(ModelResource):

    class Meta:
        queryset = PersonModel.objects.all()
        list_allowed_methods = ['get','post']
        resource_name = "PersonModel"
