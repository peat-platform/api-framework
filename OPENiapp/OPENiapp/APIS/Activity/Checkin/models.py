from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniCheckin(GenericModel):
    # id is missing because it is the default
    Place = models.ForeignKey(PlaceModel)
    text = models.TextField()