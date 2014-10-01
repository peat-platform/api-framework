__author__ = 'mpetyx'


from django.db import models
from OPENiapp.APIS.Products_and_Services.Order.models import OpeniOrder
from OPENiapp.APIS.models import GenericModel
from OPENiapp.APIS.Products_and_Services.Product.models import OpeniProduct
from OPENiapp.APIS.Products_and_Services.Service.models import OpeniService

class ProductList(models.Model):
    object_id=models.ForeignKey(OpeniProduct, null=True, blank=True)
    quantity=models.PositiveIntegerField()
    cost= models.FloatField()

class ServiceList(models.Model):
    object_id=models.ForeignKey(OpeniService, null=True, blank=True)
    quantity=models.PositiveIntegerField()
    cost= models.FloatField()

class OpeniInvoice(GenericModel):
    product_list = models.ForeignKey(ProductList, null=True, blank=True)	#A list of the ordered products/services with their quantity {object_id, count}		list of properties
    service_list = models.ForeignKey(ServiceList, null=True, blank=True)
    target_id = models.ForeignKey(OpeniOrder)
    amount = models.FloatField()
    vat = models.FloatField()
    total_amount = models.FloatField()
    currency = models.TextField()

