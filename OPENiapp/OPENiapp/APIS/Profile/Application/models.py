from django.db import models
from OPENiapp.APIS.models import *


class AdTypeModel(models.Model):
    adtypes = models.TextField()


class AdServices(models.Model):
    adservices = models.TextField()


class AdNetworks(models.Model):
    adnetworks = models.TextField()


class OpeniApplication(GenericModel):
    # id is missing because it is the default
    Application = models.ForeignKey(ApplicationModel, blank=True, null=True)
    adtype = models.ForeignKey(AdTypeModel)
    adservices = models.ForeignKey(AdServices)
    adnetworks = models.ForeignKey(AdNetworks)