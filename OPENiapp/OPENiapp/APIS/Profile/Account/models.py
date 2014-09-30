from django.db import models
from OPENiapp.APIS.commonModels import *

<<<<<<< HEAD
=======
from OPENiapp.APIS.Products_and_services.Wallet import OpeniWallet
from OPENiapp.APIS.Profile.User import OpeniUser
>>>>>>> FETCH_HEAD

class OpeniAccount(GenericModel):
    Person = models.ForeignKey(PersonModel)
    Wallet = models.ForeignKey(OpeniWallet)
    User = models.ForeignKey(OpeniUser)
    cbsid = models.TextField()
    username = models.TextField()
    email = models.TextField()
    validated = models.BooleanField()
    active = models.BooleanField()