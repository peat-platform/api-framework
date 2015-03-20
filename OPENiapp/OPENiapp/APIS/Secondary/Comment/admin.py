from django.contrib import admin
from .models import OpeniComment
from OPENiapp.admin import api_admin


class CommentAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniComment, CommentAdmin)