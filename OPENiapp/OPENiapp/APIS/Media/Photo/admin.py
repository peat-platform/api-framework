__author__ = 'mpetyx'

from django.contrib import admin
from models import OpeniPhoto
from OPENiapp.admin import api_admin


class PhotoAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniPhoto, PhotoAdmin)
