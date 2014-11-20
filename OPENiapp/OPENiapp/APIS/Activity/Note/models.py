from django.db import models
from OPENiapp.APIS.models import *


class OpeniNote(GenericModel):
    # id is missing because it is the default
    title = models.TextField()
    text = models.TextField()