__author__ = 'mpetyx'

from django.contrib import admin
from models import *


class PersonAdmin(admin.ModelAdmin):
    pass

class CloudletAdmin(admin.ModelAdmin):
    pass

class RegirestedApp(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)
admin.site.register(Cloudlet, CloudletAdmin)
admin.site.register(RegisteredApplication, RegirestedApp)

