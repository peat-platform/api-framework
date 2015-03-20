__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniStatus
from OPENiapp.admin import api_admin


class StatusAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniStatus, StatusAdmin)
