from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniQuestionOption(GenericModel):
    # id is missing because it is the default
    option_id = models.TextField()
    text = models.TextField()
    target_id = models.TextField()