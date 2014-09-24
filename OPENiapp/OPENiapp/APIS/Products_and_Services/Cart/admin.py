__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniCart


class CartAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniCart, CartAdmin)
