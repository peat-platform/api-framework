from django.contrib import admin
from .models import OpeniRefund
from OPENiapp.admin import api_admin


class RefundAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniRefund, RefundAdmin)