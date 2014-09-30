from OPENiapp.APIS.Context.models import OpeniContextAwareModel

__author__ = 'mpetyx'


from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniDelivery(GenericModel):
    # id is missing because it is the default
    target_id = models.TextField()
    signature = models.TextField()