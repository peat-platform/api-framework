from django.contrib import admin
from .models import OpeniInvoice


class InvoiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniInvoice, InvoiceAdmin)