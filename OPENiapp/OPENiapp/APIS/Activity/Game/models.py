from django.db import models
from OPENiapp.APIS.models import *


class OpeniGame(GenericModel):
    # id is missing because it is the default
    title = models.TextField()
    result = models.TextField()
    metric = models.TextField()
    text = models.TextField()