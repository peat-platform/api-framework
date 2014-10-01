from django.db import models
from OPENiapp.APIS.models import *

class OpeniRSVP(GenericModel):
    # id is missing because it is the default
    rsvp = models.TextField()
    target_id = models.TextField()