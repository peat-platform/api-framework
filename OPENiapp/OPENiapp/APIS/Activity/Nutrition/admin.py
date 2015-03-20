__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniNutrition
from OPENiapp.admin import api_admin


class NutritionAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniNutrition, NutritionAdmin)
