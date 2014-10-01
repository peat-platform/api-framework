from django.db import models
from OPENiapp.APIS.models import *

class OpeniNutrition(GenericModel):
    # id is missing because it is the default
    meal = models.TextField()
    calories = models.TextField()
    fat = models.TextField()
    fiber = models.TextField()
    protein  = models.TextField()
    sodium = models.TextField()
    water = models.TextField()