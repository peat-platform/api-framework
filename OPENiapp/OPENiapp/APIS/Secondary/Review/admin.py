from django.contrib import admin
from .models import OpeniReview


class ReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpeniReview, ReviewAdmin)