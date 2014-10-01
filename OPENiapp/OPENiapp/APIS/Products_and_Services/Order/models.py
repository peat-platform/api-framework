from django.db import models
from OPENiapp.APIS.Products_and_Services.Product.models import OpeniProduct
from OPENiapp.APIS.Products_and_Services.Service.models import OpeniService
from OPENiapp.APIS.Products_and_Services.Shop.models import OpeniShop
from OPENiapp.APIS.commonModels import GenericModel

class ProductList(models.Model):
    object_id=models.ForeignKey(OpeniProduct, null=True, blank=True)
    quantity=models.PositiveIntegerField()
    cost= models.FloatField()

class ServiceList(models.Model):
    object_id=models.ForeignKey(OpeniService, null=True, blank=True)
    quantity=models.PositiveIntegerField()
    cost= models.FloatField()


class OpeniOrder(GenericModel):
    # id is missing because it is the default
    product_list = models.ForeignKey(ProductList, null=True, blank=True)	#A list of the ordered products/services with their quantity {object_id, count}		list of properties
    service_list = models.ForeignKey(ServiceList, null=True, blank=True)
    target_id = models.ForeignKey(OpeniShop)
    amount = models.FloatField()
    vat = models.FloatField()
    total_amount = models.FloatField()
    currency = models.TextField()



