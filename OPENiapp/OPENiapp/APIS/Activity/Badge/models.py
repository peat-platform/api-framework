from django.db import models
from OPENiapp.APIS.models import *


class OpeniBadge(GenericModel):
    # id is missing because it is the default
    title = models.TextField()
    description = models.TextField()
    icon = models.TextField()