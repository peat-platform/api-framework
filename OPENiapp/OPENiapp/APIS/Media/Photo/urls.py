__author__ = 'mpetyx'

from tastypie.api import Api
from .Resources import PhotoResource

api = Api(api_name='media')
api.register(PhotoResource())

urlpatterns = api.urls