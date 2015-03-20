__author__ = 'mpetyx'

from django.contrib import admin
from .models import *
from OPENiapp.admin import api_admin


class VideoAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniVideo, VideoAdmin)
