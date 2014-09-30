from django.db import models
from OPENiapp.APIS.commonModels import *

class OpeniFriendship(GenericModel):
    # id is missing because it is the default
    target_id = models.TextField()