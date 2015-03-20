__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniNote
from OPENiapp.admin import api_admin


class NoteAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniNote, NoteAdmin)
