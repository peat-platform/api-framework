from django.contrib import admin
from .models import OpeniPayment


class PaymentAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniPayment, PaymentAdmin)