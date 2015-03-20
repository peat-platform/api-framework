from django.contrib import admin
from .models import OpeniDislike
from OPENiapp.admin import api_admin


class DislikeAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniDislike, DislikeAdmin)