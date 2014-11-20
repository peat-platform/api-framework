from django.db import models
from OPENiapp.APIS.models import *


class OpeniFavorite(GenericModel):
    # id is missing because it is the default
    target_id = models.TextField()