from OPENiapp.APIS.resources import DurationResource, LocationResource

__author__ = 'mpetyx'


from tastypie import fields
from .models import OpeniWorkout

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta

class WorkoutResource(GenericResource):
    Location = fields.ForeignKey(LocationResource, 'Location', null=True, blank=True)
    Duration = fields.ForeignKey(DurationResource, 'Duration', null=True, blank=True)
    class Meta(GenericMeta):
        queryset = OpeniWorkout.objects.all()
        resource_name = 'Workout'

