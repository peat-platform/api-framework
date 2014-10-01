from django.db import models
from OPENiapp.APIS.models import *
from django.contrib.auth.models import User as OpeniUser
from OPENiapp.APIS.Products_and_Services.Wallet.models import OpeniWallet

class OpeniAccount(GenericModel):
    Person = models.ForeignKey(PersonModel)
    Wallet = models.ForeignKey(OpeniWallet)
    User = models.ForeignKey(OpeniUser)
    cbsid = models.TextField()
    username = models.TextField()
    email = models.TextField()
    validated = models.BooleanField()
    active = models.BooleanField()