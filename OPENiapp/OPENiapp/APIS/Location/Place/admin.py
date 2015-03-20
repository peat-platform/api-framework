__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniPlace
from OPENiapp.admin import api_admin


class PlaceAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniPlace, PlaceAdmin)
