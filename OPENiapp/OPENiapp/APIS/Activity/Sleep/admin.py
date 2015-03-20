__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniSleep
from OPENiapp.admin import api_admin


class SleepAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniSleep, SleepAdmin)
