__author__ = 'mpetyx'
from OPENiapp.APIS.commonModels import GenericModel

from django.db import models


class OpeniOffer(GenericModel):
    # id is missing because it is the default
    price = models.FloatField()	#the new price that applies to the product		string
    currency = models.TextField()	#the currency for the price		string
    target_id = models.TextField()	#The id of the object where this offer applies.		string