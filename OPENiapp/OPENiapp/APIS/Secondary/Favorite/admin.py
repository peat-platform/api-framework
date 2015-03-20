from django.contrib import admin
from .models import OpeniFavorite
from OPENiapp.admin import api_admin


class FavoriteAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniFavorite, FavoriteAdmin)