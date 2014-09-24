from django.contrib import admin
from .models import OpeniGroup


class GroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniGroup, GroupAdmin)
