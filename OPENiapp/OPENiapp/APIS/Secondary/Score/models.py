__author__ = 'mpetyx'


from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniScore(GenericModel):
    # id is missing because it is the default
    value = models.TextField()
    target_id = models.TextField()