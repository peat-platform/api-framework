from django.contrib import admin
from .models import OpeniQuestionOption
from OPENiapp.admin import api_admin


class QuestionOptionAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniQuestionOption, QuestionOptionAdmin)