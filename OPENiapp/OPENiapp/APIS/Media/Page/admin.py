__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniPage
from OPENiapp.admin import api_admin


class PageAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniPage, PageAdmin)
