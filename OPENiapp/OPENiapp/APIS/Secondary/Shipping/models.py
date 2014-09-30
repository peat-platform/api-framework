__author__ = 'mpetyx'


from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniShipping(GenericModel):
    # id is missing because it is the default
    Duration = models.ForeignKey(DurationModel, blank=True, null=True)
    target_id = models.TextField()