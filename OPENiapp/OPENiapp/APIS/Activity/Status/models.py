from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniStatus(GenericModel):
    # id is missing because it is the default
    title = models.TextField()
    text = models.TextField()