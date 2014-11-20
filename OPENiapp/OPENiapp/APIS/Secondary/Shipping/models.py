from django.db import models
from OPENiapp.APIS.models import GenericModel, DurationModel, AddressModel
from OPENiapp.APIS.Products_and_Services.Order.models import OpeniOrder


class OpeniShipping(GenericModel):
    # id is missing because it is the default
    target_id = models.ForeignKey(OpeniOrder) #The id of the order or shipping where this delivery applies		string
    Duration = models.OneToOneField(DurationModel)    #The URL to the signature of the user that received the delivery
    Address = models.OneToOneField(AddressModel)
    details = models.TextField()
