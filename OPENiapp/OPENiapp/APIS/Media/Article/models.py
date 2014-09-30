from OPENiapp.APIS.commonModels import *

__author__ = 'mpetyx'


from django.db import models

__all__ = ["OpeniArticle",]
class OpeniArticle(GenericModel):
    # id is missing because it is the default
    service = models.TextField()
    File = models.ForeignKey(FileModel)
    duration = models.TextField()
    Tags = models.ForeignKey(TagsModel)
    text = models.TextField()