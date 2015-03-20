__author__ = 'mpetyx'

from django.contrib import admin

from .models import OpeniCheckin
from OPENiapp.admin import api_admin


class CheckinAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniCheckin, CheckinAdmin)
