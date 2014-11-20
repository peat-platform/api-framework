__author__ = 'alvertisjo'
from django.db import models

from OPENiapp.APIS.models import GenericModel
from OPENiapp.APIS.models import *


class OpeniOffer(GenericModel):
    # id is missing because it is the default
    price = models.TextField()
    Duration = models.ForeignKey(DurationModel, blank=True, null=True)
    currency = models.TextField()
    target_id = models.TextField()