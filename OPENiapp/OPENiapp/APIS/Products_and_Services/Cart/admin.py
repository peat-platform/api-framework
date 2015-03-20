__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniCart
from OPENiapp.admin import api_admin


class CartAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniCart, CartAdmin)
