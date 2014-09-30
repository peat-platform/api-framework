from OPENiapp.APIS.Context.models import OpeniContextAwareModel
from OPENiapp.APIS.Context.models import OpeniContext
from OPENiapp.APIS.commonModels import *

__author__ = 'mpetyx'


from django.db import models

__all__ = ["OpeniArticle",]
class OpeniArticle(OpeniContextAwareModel):
    # id is missing because it is the default
    url = models.TextField()
    object_type = models.TextField()
    service = models.TextField()
    From = models.TextField()
    File = models.TextField()
    duration = models.TextField()
    Time = models.TextField()
    tags = models.TextField()
    text = models.TextField()

