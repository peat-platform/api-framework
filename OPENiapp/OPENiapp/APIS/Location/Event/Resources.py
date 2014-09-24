__author__ = 'mpetyx'

from .models import OpeniEvent

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta


class EventResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniEvent.objects.all()
        resource_name = 'Event'