from django.contrib import admin
from .models import OpeniReview
from OPENiapp.admin import api_admin


class ReviewAdmin(admin.ModelAdmin):
    pass


api_admin.register(OpeniReview, ReviewAdmin)