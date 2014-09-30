__author__ = 'alvertisjo'


from django.db import models
from OPENiapp.APIS.commonModels import GenericModel
from OPENiapp.APIS.Products_and_Services.Service.models import ServiceModel

class OpeniScore(GenericModel):
    # id is missing because it is the default
    score = models.FloatField()
    target_id = models.TextField()