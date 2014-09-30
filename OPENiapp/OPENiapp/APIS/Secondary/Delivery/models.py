__author__ = 'mpetyx'

from django.db import models
from OPENiapp.APIS.commonModels import GenericModel
from OPENiapp.APIS.Secondary.Shipping.models import OpeniShipping


class OpeniDelivery(GenericModel):
    # id is missing because it is the default
    target_id = models.ForeignKey(OpeniShipping) #The id of the order or shipping where this delivery applies		string
    signature = models.TextField()	#The URL to the signature of the user that received the delivery

