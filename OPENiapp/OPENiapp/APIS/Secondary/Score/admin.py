from django.contrib import admin
from .models import OpeniScore
from OPENiapp.admin import api_admin


class ScoreAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniScore, ScoreAdmin)