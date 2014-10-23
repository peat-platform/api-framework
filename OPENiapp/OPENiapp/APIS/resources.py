__author__ = 'mpetyx'

from tastypie.resources import ModelResource
from OPENiapp.APIS.models import *


class PersonModelResource(ModelResource):

    class Meta:
        queryset = PersonModel.objects.all()
        list_allowed_methods = ['get','post']
        resource_name = "PersonModel"

class FromResource(ModelResource):

    class Meta:
        queryset = FromModel.objects.all()
        resource_name = "From"

class TimeResource(ModelResource):

    class Meta:
        queryset = TimeModel.objects.all()
        resource_name = "Time"

class DurationResource(ModelResource):

    class Meta:
        queryset = DurationModel.objects.all()
        resource_name = "Duration"