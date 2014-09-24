from django.contrib import admin
from .models import OpeniDislike


class DislikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniDislike, DislikeAdmin)