__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniPage


class PageAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniPage, PageAdmin)
