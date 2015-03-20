__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniOrder
from OPENiapp.admin import api_admin


class OrderAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniOrder, OrderAdmin)
