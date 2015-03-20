from django.contrib import admin
from .models import OpeniFriendship
from OPENiapp.admin import api_admin


class FriendshipAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniFriendship, FriendshipAdmin)