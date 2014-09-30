from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniComment(GenericModel):
    # id is missing because it is the default
    title = models.TextField()
    text = models.TextField()
    target_id = models.TextField()