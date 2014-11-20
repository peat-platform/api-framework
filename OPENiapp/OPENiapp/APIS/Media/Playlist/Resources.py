__author__ = 'mpetyx'

from .models import OpeniPlaylist

from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication
from OPENiapp.APIS.OPENIResource import OpeniResource


class PlaylistResource(OpeniResource):
    class Meta(GenericMeta):
        queryset = OpeniPlaylist.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Playlist'
        authentication = Authentication()
        authorization = Authorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }