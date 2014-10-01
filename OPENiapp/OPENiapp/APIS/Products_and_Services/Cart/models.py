from django.db import models
from OPENiapp.APIS.models import *
from OPENiapp.APIS.Products_and_Services.Product.models import OpeniProduct
from OPENiapp.APIS.Products_and_Services.Service.models import OpeniService
from OPENiapp.APIS.Products_and_Services.Shop.models import OpeniShop

class CartProductList(models.Model):
    object_id=models.ForeignKey(OpeniProduct, null=True, blank=True)
    quantity=models.PositiveIntegerField()

class CartServiceList(models.Model):
    object_id=models.ForeignKey(OpeniService, null=True, blank=True)
    quantity=models.PositiveIntegerField()


class OpeniCart(GenericModel):
    # id is missing because it is the default
    product_list = models.ForeignKey(CartProductList, null=True, blank=True)	#A list of the ordered products/services with their quantity {object_id, count}		list of properties
    service_list = models.ForeignKey(CartServiceList, null=True, blank=True)
    target_id= models.ManyToManyField(OpeniShop)#the shop id where this order has been generated from.		string
