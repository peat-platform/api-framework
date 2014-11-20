from django.db import models
from django.contrib.auth.models import User as OpeniUser

from OPENiapp.APIS.models import *
from OPENiapp.APIS.Products_and_Services.Wallet.models import OpeniWallet


class OpeniAccount(GenericModel):
    Person = models.ForeignKey(PersonModel, blank=True, null=True)
    Wallet = models.ForeignKey(OpeniWallet, blank=True, null=True)
    User = models.ForeignKey(OpeniUser, blank=True, null=True)
    cbsid = models.TextField()
    username = models.TextField()
    email = models.TextField()
    validated = models.BooleanField()
    active = models.BooleanField()