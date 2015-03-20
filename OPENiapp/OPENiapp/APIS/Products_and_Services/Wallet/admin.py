__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniWallet
from OPENiapp.admin import api_admin


class WalletAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniWallet, WalletAdmin)
