from django.contrib import admin
from .models import OpeniOffer


class OfferAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniOffer, OfferAdmin)