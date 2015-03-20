__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniContext
from OPENiapp.admin import api_admin


class ContextAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniContext, ContextAdmin)
