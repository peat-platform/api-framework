from django.contrib import admin
from .models import OpeniQuestionOption


class QuestionOptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniQuestionOption, QuestionOptionAdmin)