from OPENiapp.APIS.models import *

__author__ = 'mpetyx'


from django.db import models
from OPENiapp.APIS.models import FileModel, TagsModel


__all__ = ["OpeniArticle",]
class OpeniArticle(GenericModel):
    # id is missing because it is the default
    File = models.ForeignKey(FileModel)
    duration = models.TextField()
    Tags = models.ForeignKey(TagsModel)
    text = models.TextField()