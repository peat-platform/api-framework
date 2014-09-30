__author__ = 'mpetyx'


from django.db import models
from OPENiapp.APIS.commonModels import GenericModel

class OpeniReview(GenericModel):
    # id is missing because it is the default
    title = models.TextField()	#When available, a title of the review		string
    text = models.TextField()	#Free text of the review, if available		string
    rating= models.FloatField()	#The quantitative value of the rating (optional)		string
    scale= models.IntegerField()	#The scale of rating (optional)		string
    target_id= models.TextField()	#The id of the object where this review is targeted		string
