__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniActivityEvent

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta

class ActivityEventResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniActivityEvent.objects.all()
        resource_name = 'Activityevent'
