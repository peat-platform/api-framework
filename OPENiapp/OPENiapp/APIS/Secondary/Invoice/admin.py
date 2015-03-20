from django.contrib import admin
from .models import OpeniInvoice
from OPENiapp.admin import api_admin


class InvoiceAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniInvoice, InvoiceAdmin)