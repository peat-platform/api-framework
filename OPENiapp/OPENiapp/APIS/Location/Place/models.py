
__author__ = 'mpetyx'


from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniPlace(GenericModel):
    # id is missing because it is the default
    text = models.TextField()
    Place = models.ForeignKey(PlaceModel, blank=True, null=True)