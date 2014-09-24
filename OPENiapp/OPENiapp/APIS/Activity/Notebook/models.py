
__author__ = 'mpetyx'


from django.db import models
from OPENiapp.APIS.Context.models import OpeniContextAwareModel


class OpeniNotebook(OpeniContextAwareModel):
    # id is missing because it is the default
    pass
