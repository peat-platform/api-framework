from django.contrib import admin
from .models import OpeniLike


class LikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniLike, LikeAdmin)