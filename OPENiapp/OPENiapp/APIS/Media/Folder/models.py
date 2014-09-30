
__author__ = 'mpetyx'

from django.db import models
from OPENiapp.APIS.commonModels import *


class OpeniFolder(GenericModel):
    # id is missing because it is the default
    File = models.ForeignKey(FileModel, blank=True, null=True)
    data = models.TextField()