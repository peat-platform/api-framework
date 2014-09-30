from OPENiapp.APIS.Context.models import OpeniContextAwareModel

__author__ = 'mpetyx'


from django.db import models




class ProductProfile(models.Model):
    name = models.TextField() #The name of the product		string
    description = models.TextField()	#Any description for a product		string
    category = models.TextField()	#The categories the product may belong		list of strings
    picture = models.TextField()	#A picture of the product		string
    #company	The company that produces the product		An [[Profile#Organization
    year = models.IntegerField()	#The year the product became available for the first time		string


class OpeniProduct(OpeniContextAwareModel):
    # id is missing because it is the default
    url = models.TextField()
    object_type = models.TextField()
    service = models.TextField()
    From = models.TextField()
    price = models.FloatField()
    currency = models.TextField()
    amount = models.TextField()
    code = models.TextField()
    profile = models.ForeignKey(ProductProfile)
