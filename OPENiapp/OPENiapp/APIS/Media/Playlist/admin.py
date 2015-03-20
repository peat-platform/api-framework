__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniPlaylist
from OPENiapp.admin import api_admin


class PlaylistAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniPlaylist, PlaylistAdmin)
