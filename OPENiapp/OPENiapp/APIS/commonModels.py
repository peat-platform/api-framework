from OPENiapp.OPENiapp.APIS.Context.models import OpeniContextAwareModel

from OPENiapp.OPENiapp.APIS.Profile.Account.models import OpeniAccount

from django.db import models

class GenericModel(OpeniContextAwareModel):
    object_type = models.TextField(null=True)
    service = models.TextField(null=True)
    url = models.TextField(null=True)
    from_ = models.ForeignKey(OpeniAccount,null=True, on_delete=models.DO_NOTHING)
    #time = 
    #models.ForeignKey(OpeniContext,null=True, on_delete=models.DO_NOTHING)