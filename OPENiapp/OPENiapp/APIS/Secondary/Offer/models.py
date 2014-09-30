from OPENiapp.APIS.Context.models import OpeniContextAwareModel

__author__ = 'mpetyx'


from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniOffer(GenericModel):
    # id is missing because it is the default
    price = models.TextField()
    Duration = models.ForeignKey(DurationModel, blank=True, null=True)
    currency = models.TextField()
    target_id = models.TextField()