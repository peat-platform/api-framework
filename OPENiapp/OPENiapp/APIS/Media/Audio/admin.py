__author__ = 'mpetyx'

from django.contrib import admin
from .models import *
from OPENiapp.admin import api_admin


class AudioAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniAudio, AudioAdmin)
