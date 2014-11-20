from OPENiapp.APIS.models import LocationModel, TagsModel, GenericModel, BaseFileModel

__author__ = 'mpetyx'

from django.db import models

__all__ = ["OpeniPhoto", ]


class OpeniPhoto(GenericModel):
    # id is missing because it is the default
    BaseFile = models.ForeignKey(BaseFileModel)
    Location = models.ForeignKey(LocationModel, blank=True, null=True)
    Tags = models.ForeignKey(TagsModel, blank=True, null=True)
    width = models.TextField()
    height = models.TextField()
