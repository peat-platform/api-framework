from django.db import models
from OPENiapp.APIS.models import *


class OpeniWorkout(GenericModel):
    # id is missing because it is the default
    Location = models.ForeignKey(LocationModel, blank=True, null=True)
    Duration = models.ForeignKey(DurationModel, blank=True, null=True)
    text = models.TextField()
    equipment = models.TextField()
    distance = models.TextField()
    metric = models.TextField()
    previous_id = models.TextField()
    next_id = models.TextField()