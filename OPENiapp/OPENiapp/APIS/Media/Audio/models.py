__author__ = 'mpetyx'

from django.db import models
from OPENiapp.APIS.models import *


class OpeniAudio(GenericModel):
    # id is missing because it is the default
    BaseFile = models.ForeignKey(BaseFileModel, blank=True, null=True)
    Duration = models.ForeignKey(DurationModel, blank=True, null=True)
    Tags = models.ForeignKey(TagsModel, blank=True, null=True)
    text = models.TextField()