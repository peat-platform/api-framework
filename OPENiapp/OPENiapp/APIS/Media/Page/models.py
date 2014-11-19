
__author__ = 'mpetyx'

from django.db import models
from OPENiapp.APIS.models import *

class OpeniPage(GenericModel):
    # id is missing because it is the default
    BaseFile = models.ForeignKey(BaseFileModel, blank=True, null=True)
    data = models.TextField()
