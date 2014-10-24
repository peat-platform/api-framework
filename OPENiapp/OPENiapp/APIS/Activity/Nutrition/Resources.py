__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniNutrition

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class NutritionResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniNutrition.objects.all()
        resource_name = 'Nutrition'
