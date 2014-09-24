__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniTravel


class TravelAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniTravel, TravelAdmin)
