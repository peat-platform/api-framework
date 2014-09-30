__author__ = 'alvertisjo'
from OPENiapp.APIS.commonModels import GenericModel

from django.db import models
from OPENiapp.APIS.commonModels import *


class OpeniOffer(GenericModel):
    # id is missing because it is the default
    price = models.TextField()
    Duration = models.ForeignKey(DurationModel, blank=True, null=True)
    currency = models.TextField()
    target_id = models.TextField()