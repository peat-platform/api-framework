__author__ = 'mpetyx'

from django.contrib import admin
from .models import *
from OPENiapp.admin import api_admin


class FileAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniFile, FileAdmin)
