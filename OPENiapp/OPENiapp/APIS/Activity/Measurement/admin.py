__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniMeasurement
from OPENiapp.admin import api_admin


class MeasurementAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniMeasurement, MeasurementAdmin)
