
__author__ = 'mpetyx'

from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniPlaylist(GenericModel):
    # id is missing because it is the default
    File = models.ForeignKey(FileModel, blank=True, null=True)
    Duration = models.ForeignKey(DurationModel, blank=True, null=True)
    Tags = models.ForeignKey(TagsModel, blank=True, null=True)
    data = models.TextField()