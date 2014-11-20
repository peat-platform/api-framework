from django.db import models
from OPENiapp.APIS.models import *


class OpeniTag(GenericModel):
    # id is missing because it is the default
    text = models.TextField()
    tagged_id = models.TextField()
    target_id = models.TextField()