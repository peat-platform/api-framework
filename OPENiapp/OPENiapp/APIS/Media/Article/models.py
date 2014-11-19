__author__ = 'mpetyx'


from django.db import models
from OPENiapp.APIS.models import BaseFileModel, TagsModel
from OPENiapp.APIS.models import *
from OPENiapp.APIS.models import DurationModel

__all__ = ["OpeniArticle",]
class OpeniArticle(GenericModel):
    # id is missing because it is the default
    BaseFile = models.ForeignKey(BaseFileModel)
    Duration = models.ForeignKey(DurationModel,blank=True, null=True)
    Tags = models.ForeignKey(TagsModel,blank=True, null=True)
    text = models.TextField()