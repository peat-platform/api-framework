__author__ = 'mpetyx'

from django.contrib import admin
from .models import FromModel
from OPENiapp.admin import api_admin


class FromAdmin(admin.ModelAdmin):
    pass


api_admin.register(FromModel, FromAdmin)
