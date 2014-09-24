from django.contrib import admin
from .models import OpeniTag


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniTag, TagAdmin)