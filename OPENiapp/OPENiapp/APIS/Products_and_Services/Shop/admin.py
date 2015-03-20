__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniShop
from OPENiapp.admin import api_admin


class ShopAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniShop, ShopAdmin)
