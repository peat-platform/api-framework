from django.contrib import admin
from .models import OpeniOffer
from OPENiapp.admin import api_admin


class OfferAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniOffer, OfferAdmin)