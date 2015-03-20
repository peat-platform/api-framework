__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniArticle
from OPENiapp.admin import api_admin


class ArticleAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniArticle, ArticleAdmin)
