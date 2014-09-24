__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniPlace


class PlaceAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniPlace, PlaceAdmin)
