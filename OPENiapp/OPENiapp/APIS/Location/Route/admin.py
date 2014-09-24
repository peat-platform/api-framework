__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniRoute


class RouteAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniRoute, RouteAdmin)
