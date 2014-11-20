__author__ = 'alvertisjo'

from django.db import models
from OPENiapp.APIS.models import GenericModel, ProductModel


class OpeniProduct(GenericModel):
    # id is missing because it is the default
    Profile = models.OneToOneField(ProductModel)
    price = models.FloatField()
    currency = models.TextField()
    amount = models.PositiveIntegerField() #available products in a store, if available
    code = models.TextField()
