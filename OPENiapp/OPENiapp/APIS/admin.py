__author__ = 'mpetyx'

from django.contrib import admin
from .models import FromModel


class FromAdmin(admin.ModelAdmin):
    pass


admin.site.register(FromModel, FromAdmin)
