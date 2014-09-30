__author__ = 'mpetyx'


from tastypie.authorization import DjangoAuthorization
from .models import OpeniAccount

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication

class AccountResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniAccount.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Account'
        authentication = Authentication()
        authorization = Authorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }

        extra_actions = [
            {
                "name": "checkins",
                "http_method": "GET",
                "description": "Retrieve a list of Account Checkins",
                "fields": {}
            },
            # Not yet implemented or used
            #{
            #    "name": "checkins",
            #    "http_method": "POST",
            #    "description": "Post a Checkin",
            #    "fields": {}
            #}
        ]