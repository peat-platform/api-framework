from django.db import models
from OPENiapp.APIS.models import *

class OpeniCheckin(GenericModel):
    # id is missing because it is the default
    Place = models.ForeignKey(PlaceModel,blank=True, null=True)
    text = models.TextField()