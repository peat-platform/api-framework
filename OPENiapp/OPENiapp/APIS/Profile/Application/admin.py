__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniApplication
from OPENiapp.admin import api_admin


class ApplicationAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniApplication, ApplicationAdmin)
