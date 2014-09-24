from django.contrib import admin
from .models import OpeniRefund


class RefundAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniRefund, RefundAdmin)