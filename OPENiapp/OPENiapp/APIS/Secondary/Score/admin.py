from django.contrib import admin
from .models import OpeniScore


class ScoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniScore, ScoreAdmin)