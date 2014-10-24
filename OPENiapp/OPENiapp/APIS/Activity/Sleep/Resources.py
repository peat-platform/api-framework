__author__ = 'mpetyx'


from tastypie import fields
from .models import OpeniSleep
from OPENiapp.APIS.resources import DurationResource
from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta

class SleepResource(GenericResource):
    Duration = fields.ForeignKey(DurationResource, 'Duration', null=True, blank=True)
    class Meta(GenericMeta):
        queryset = OpeniSleep.objects.all()
        resource_name = 'Sleep'
