__author__ = 'mpetyx'


from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniReview(GenericModel):
    # id is missing because it is the default
    title = models.TextField()
    text = models.TextField()
    rating = models.TextField()
    scale = models.TextField()
    target_id = models.TextField()