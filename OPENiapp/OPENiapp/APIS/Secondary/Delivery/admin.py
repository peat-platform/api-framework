from django.contrib import admin
from .models import OpeniDelivery


class DeliveryAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniDelivery, DeliveryAdmin)