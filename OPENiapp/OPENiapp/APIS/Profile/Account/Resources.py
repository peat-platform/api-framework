__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniAccount
from tastypie import fields
from OPENiapp.APIS.models import *
from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication
from OPENiapp.APIS.resources import PersonModelResource
from django.contrib.auth.models import User as OpeniUser
from OPENiapp.APIS.Products_and_Services.Wallet.models import OpeniWallet

class AccountResource(GenericResource):
    Person = fields.ForeignKey(PersonModelResource, 'Person', null=True, blank=True)
    class Meta(GenericMeta):
        queryset = OpeniAccount.objects.all()
        resource_name = 'Account'

        extra_actions = [
            {
                "name": "checkins",
                "http_method": "GET",
                "description": "Retrieve a list of Account Checkins",
                "fields": {}
            },
        ]