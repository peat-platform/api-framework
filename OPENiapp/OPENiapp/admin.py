__author__ = 'mpetyx'

from django.contrib import admin
from models import *
from django.contrib.admin import AdminSite


class PersonAdmin(admin.ModelAdmin):
    pass

class CloudletAdmin(admin.ModelAdmin):
    pass

class RegirestedApp(admin.ModelAdmin):
    pass

class APIAdminSite(AdminSite):
    site_header = 'API Framework Administration'

api_admin = APIAdminSite(name='apiadmin')
api_admin.register(Person, PersonAdmin)
api_admin.register(Cloudlet, CloudletAdmin)
api_admin.register(RegisteredApplication, RegirestedApp)

from allauth.socialaccount.models import SocialAccount, SocialApp,SocialToken

class SocialAppsAdminSite(AdminSite):
    site_header = 'Social APPs  Administration'

social_apps = SocialAppsAdminSite(name='socialApps')
social_apps.register(SocialAccount)
social_apps.register(SocialApp)
social_apps.register(SocialToken)