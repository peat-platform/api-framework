__author__ = 'mpetyx'


from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniPayment(GenericModel):
    # id is missing because it is the default
    target_id = models.TextField()
    card_id = models.TextField()
    amount = models.TextField()
    vat = models.TextField()
    total = models.TextField()
    currency = models.TextField()