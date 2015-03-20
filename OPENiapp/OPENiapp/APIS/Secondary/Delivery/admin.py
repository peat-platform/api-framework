from django.contrib import admin
from .models import OpeniDelivery
from OPENiapp.admin import api_admin


class DeliveryAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniDelivery, DeliveryAdmin)