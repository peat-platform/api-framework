__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniBadge
from OPENiapp.admin import api_admin


class BadgeAdmin(admin.ModelAdmin):
    pass

api_admin.register(OpeniBadge, BadgeAdmin)

