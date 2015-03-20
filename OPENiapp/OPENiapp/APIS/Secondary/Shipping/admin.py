from django.contrib import admin
from .models import OpeniShipping
from OPENiapp.admin import api_admin


class ShippingAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniShipping, ShippingAdmin)