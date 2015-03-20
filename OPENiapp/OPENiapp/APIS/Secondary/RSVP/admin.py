from django.contrib import admin
from .models import OpeniRSVP
from OPENiapp.admin import api_admin


class RSVPAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniRSVP, RSVPAdmin)