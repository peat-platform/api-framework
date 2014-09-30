__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniWallet


class WalletAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniWallet, WalletAdmin)
