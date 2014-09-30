from OPENiapp.APIS.Context.models import OpeniContextAwareModel
from django.db import models

class OpeniEvent(GenericModel):
    # id is missing because it is the default
    Place = models.ForeignKey(PlaceModel)
    Duration = models.ForeignKey(DurationModel)
    description = models.TextField()
    picture = models.TextField()
    title = models.TextField()