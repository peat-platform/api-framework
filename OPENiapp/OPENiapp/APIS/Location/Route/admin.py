__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniRoute
from OPENiapp.admin import api_admin


class RouteAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniRoute, RouteAdmin)
