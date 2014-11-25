__author__ = 'mpetyx'

from .models import OpeniPlaylist

from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication
from OPENiapp.APIS.OPENIResource import OpeniResource


class PlaylistResource(OpeniResource):
    class Meta(GenericMeta):
        object_class = OpeniPlaylist
        resource_name = 'Playlist'
