__author__ = 'mpetyx'


from .models import OpeniBadge

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication


class BadgeResource(GenericResource):
    class Meta(GenericMeta):
        queryset = OpeniBadge.objects.all()
        resource_name = 'Badge'

