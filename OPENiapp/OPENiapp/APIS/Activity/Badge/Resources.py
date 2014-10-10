__author__ = 'mpetyx'


from .models import OpeniBadge

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from tastypie import fields
from cloudletClient.CloudletResource import CloudletResource

class BadgeResource(CloudletResource): #GenericResource):
    # uuid = fields.CharField(attribute='uuid')
    # title = fields.CharField(attribute='title')
    # description = fields.CharField(attribute='description')
    # icon = fields.CharField(attribute='icon')


    class Meta(GenericMeta):
        # queryset = OpeniBadge.objects.all()
        object_class = OpeniBadge
        resource_name = 'Badge'
        excludes = ['id']