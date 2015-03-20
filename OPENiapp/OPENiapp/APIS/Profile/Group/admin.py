from django.contrib import admin
from .models import OpeniGroup
from OPENiapp.admin import api_admin


class GroupAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniGroup, GroupAdmin)
