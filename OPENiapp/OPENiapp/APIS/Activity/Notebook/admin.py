__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniNotebook
from OPENiapp.admin import api_admin


class NotebookAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniNotebook, NotebookAdmin)
