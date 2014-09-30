from django.db import models
from OPENiapp.APIS.Context.models import OpeniContextAwareModel
from OPENiapp.APIS.Products_and_Services.Product.models import OpeniProduct
from OPENiapp.APIS.Products_and_Services.Shop.models import OpeniShop


class OpeniOrder(OpeniContextAwareModel):
    # id is missing because it is the default
    url = models.TextField()
    object_type = models.TextField()
    service = models.TextField()
    From = models.TextField()
    list = models.ManyToManyField(OpeniProduct)
    target_id = models.ForeignKey(OpeniShop)
    amount = models.FloatField()
    vat = models.FloatField()
    total_amount = models.FloatField()
    currency = models.TextField()


