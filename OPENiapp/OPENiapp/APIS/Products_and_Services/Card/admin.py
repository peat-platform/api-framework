__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniCard
from OPENiapp.admin import api_admin


class CardAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniCard, CardAdmin)
