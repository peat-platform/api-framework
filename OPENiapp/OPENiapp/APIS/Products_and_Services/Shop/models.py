__author__ = 'alvertisjo'

from django.db import models
from OPENiapp.APIS.models import GenericModel, PlaceModel


class OpeniShop(GenericModel):
    # id is missing because it is the default
    Place = models.ForeignKey(PlaceModel)
    region = models.TextField()
    currency = models.TextField()
    description = models.TextField()
