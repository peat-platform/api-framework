__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniEvent
from OPENiapp.admin import api_admin


class EventAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniEvent, EventAdmin)
