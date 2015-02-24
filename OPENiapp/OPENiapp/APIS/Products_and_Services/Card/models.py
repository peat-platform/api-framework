__author__ = 'mpetyx'

from django.db import models
from OPENiapp.APIS.models import GenericModel, AddressModel


class OpeniCard(GenericModel):
    # id is missing because it is the default
    billing_address = models.ForeignKey(AddressModel, blank=True, null=True)
    number = models.TextField()
    card_owner_date_of_birth = models.TextField()
    card_type = models.TextField()
    expiration_date = models.TextField()
    card_verification_number = models.TextField()