__author__ = 'alvertisjo'


from django.db import models
from OPENiapp.APIS.models import GenericModel
from OPENiapp.APIS.Secondary.Invoice.models import OpeniInvoice
from OPENiapp.APIS.Products_and_Services.Card.models import OpeniCard


class OpeniPayment(GenericModel):
    # id is missing because it is the default
    target_id = models.ForeignKey(OpeniInvoice)	#the id of the object where this payment applies; usually it is an [invoice]		string
    card_id= models.ForeignKey(OpeniCard)	#the id of the used payment method		string

