__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniNotebook


class NotebookAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniNotebook, NotebookAdmin)
