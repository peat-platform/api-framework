
__author__ = 'alvertisjo'


from django.db import models
from OPENiapp.APIS.commonModels import GenericModel, ServiceModel


class OpeniService(GenericModel):
    # id is missing because it is the default
    Profile = models.OneToOneRel(ServiceModel)
    price = models.FloatField()
    currency = models.TextField()
    amount = models.PositiveIntegerField() #available products in a store, if available
    code = models.TextField()