__author__ = 'mpetyx'

from django.contrib import admin
from .models import OpeniQuestion
from OPENiapp.admin import api_admin


class QuestionAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniQuestion, QuestionAdmin)
