
__author__ = 'mpetyx'

from django.db import models
from OPENiapp.APIS.models import *

__all__ = ["OpeniPhoto",]
class OpeniPhoto(GenericModel):
    # id is missing because it is the default
    profile = models.TextField()
    Location = models.ForeignKey(LocationModel)
    Tags = models.ForeignKey(TagsModel, blank=True, null=True)
    width = models.TextField()
    height = models.TextField()
