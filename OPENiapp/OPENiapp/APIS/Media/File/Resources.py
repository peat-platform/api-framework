__author__ = 'mpetyx'

from tastypie.authorization import DjangoAuthorization
from .models import OpeniFile
from tastypie import fields

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication
from OPENiapp.APIS.Secondary.Tag.Resources import TagResource
from OPENiapp.APIS.resources import DurationResource, BaseFileResource


class FileResource(GenericResource):
    Duration = fields.ForeignKey(DurationResource, 'Duration', null=True, blank=True)
    Tag = fields.ForeignKey(TagResource, 'Tag', null=True, blank=True)
    BaseFile = fields.ForeignKey(BaseFileResource, 'BaseFile')
    class Meta(GenericMeta):
        queryset = OpeniFile.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'File'
        authentication = Authentication()
        authorization = Authorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }