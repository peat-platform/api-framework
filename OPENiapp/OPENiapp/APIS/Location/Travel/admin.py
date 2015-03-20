__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniTravel
from OPENiapp.admin import api_admin


class TravelAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniTravel, TravelAdmin)
