from django.db import models
from OPENiapp.APIS.models import *

class OpeniSleep(GenericModel):
    # id is missing because it is the default
    Duration = models.ForeignKey(DurationModel)
    deep = models.TextField()
    rem = models.TextField()
    light = models.TextField()
    awake = models.TextField()
    times_woken = models.TextField()