from django.contrib import admin
from .models import OpeniRSVP


class RSVPAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniRSVP, RSVPAdmin)