from django.contrib import admin
from .models import OpeniFriendship


class FriendshipAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniFriendship, FriendshipAdmin)