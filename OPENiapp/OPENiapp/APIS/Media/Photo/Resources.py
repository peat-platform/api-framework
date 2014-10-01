__author__ = 'mpetyx'

from .models import OpeniPhoto

from OPENiapp.Providers.Facebook.connector import provider as FBprovider
from OPENiapp.Providers.Twitter.connector import provider as TWprovider
from allauth.socialaccount.models import SocialToken

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

from tastypie.serializers import Serializer
from tastypie import fields
from OPENiapp.APIS.Context.Resources import ContextResource

class PhotoResource(GenericResource):

    # journey = fields.ForeignKey(WorkJourneyResource, 'work_journey', null=True, blank=True)
    class Meta(GenericMeta):
        queryset = OpeniPhoto.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Photo'
        authentication = Authentication()
        authorization = Authorization()
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])