from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniWorkout(GenericModel):
    # id is missing because it is the default
    Location = models.ForeignKey(LocationModel)
    Duration = models.ForeignKey(DurationModel)
    text = models.TextField()
    equipment = models.TextField()
    distance = models.TextField()
    metric = models.TextField()
    previous_id = models.TextField()
    next_id = models.TextField()