__author__ = 'mpetyx'

from django.db import models
from OPENiapp.APIS.models import *


class OpeniRoute(GenericModel):
    # id is missing because it is the default
    Duration = models.ForeignKey(DurationModel, blank=True, null=True)
    title = models.TextField()
    description = models.TextField()
    picture = models.TextField()
