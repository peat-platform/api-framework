__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniService
from OPENiapp.admin import api_admin


class ServiceAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniService, ServiceAdmin)
