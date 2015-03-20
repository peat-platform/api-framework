__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniGame
from OPENiapp.admin import api_admin


class GameAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniGame, GameAdmin)
