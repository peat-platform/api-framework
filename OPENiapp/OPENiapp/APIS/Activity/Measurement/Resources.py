__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniMeasurement

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication


class MeasurementResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniMeasurement.objects.all()
        resource_name = 'Measurement'
