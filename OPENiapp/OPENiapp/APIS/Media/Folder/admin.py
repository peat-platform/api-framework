__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniFolder
from OPENiapp.admin import api_admin


class FolderAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniFolder, FolderAdmin)
