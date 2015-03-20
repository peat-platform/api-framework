__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniAccount
from OPENiapp.admin import api_admin


class AccountAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniAccount, AccountAdmin)
