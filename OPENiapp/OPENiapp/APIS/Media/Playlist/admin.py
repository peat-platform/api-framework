__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniPlaylist


class PlaylistAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniPlaylist, PlaylistAdmin)
