from django.contrib import admin
from .models import OpeniLike
from OPENiapp.admin import api_admin


class LikeAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniLike, LikeAdmin)