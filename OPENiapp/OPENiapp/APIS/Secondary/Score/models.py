__author__ = 'alvertisjo'

from django.db import models
from OPENiapp.APIS.models import GenericModel


class OpeniScore(GenericModel):
    # id is missing because it is the default
    score = models.FloatField()
    target_id = models.TextField()