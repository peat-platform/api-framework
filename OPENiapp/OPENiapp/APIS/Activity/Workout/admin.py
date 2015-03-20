__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniWorkout
from OPENiapp.admin import api_admin


class WorkoutAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniWorkout, WorkoutAdmin)
