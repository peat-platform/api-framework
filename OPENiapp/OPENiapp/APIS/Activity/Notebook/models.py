from django.db import models
from OPENiapp.APIS.models import *

from OPENiapp.APIS.Activity.Note.models import OpeniNote


class OpeniNotebook(GenericModel):
    # id is missing because it is the default
    title = models.TextField()
    description = models.TextField()
    Notes = models.ForeignKey(OpeniNote)