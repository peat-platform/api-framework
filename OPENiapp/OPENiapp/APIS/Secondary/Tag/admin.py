from django.contrib import admin
from .models import OpeniTag
from OPENiapp.admin import api_admin


class TagAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniTag, TagAdmin)