from django.contrib import admin
from .models import OpeniComment


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniComment, CommentAdmin)