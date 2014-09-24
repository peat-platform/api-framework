from django.contrib import admin
from .models import OpeniShipping


class ShippingAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniShipping, ShippingAdmin)