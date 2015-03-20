from django.contrib import admin
from .models import OpeniPayment
from OPENiapp.admin import api_admin


class PaymentAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniPayment, PaymentAdmin)