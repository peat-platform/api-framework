from django.db import models
from OPENiapp.APIS.commonModels import GenericModel
from OPENiapp.APIS.Products_and_Services.Card.models import OpeniCard


class OpeniWallet(GenericModel):
    cards = models.ForeignKey(OpeniCard, null=True, blank=True)
    name = models.TextField()
    description = models.TextField()

