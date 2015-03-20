__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniProduct
from OPENiapp.admin import api_admin


class ProductAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniProduct, ProductAdmin)
