from django.contrib import admin
from .models import OpeniFavorite


class FavoriteAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniFavorite, FavoriteAdmin)