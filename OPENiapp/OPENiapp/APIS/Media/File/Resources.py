__author__ = 'mpetyx'

from tastypie import fields

from .models import OpeniFile
from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication
from OPENiapp.APIS.Secondary.Tag.Resources import TagResource
from OPENiapp.APIS.resources import DurationResource, BaseFileResource
from OPENiapp.APIS.OPENIResource import OpeniResource


class FileResource(OpeniResource):
    Duration = fields.ForeignKey(DurationResource, 'Duration', null=True, blank=True)
    Tag = fields.ForeignKey(TagResource, 'Tag', null=True, blank=True)
    BaseFile = fields.ForeignKey(BaseFileResource, 'BaseFile', null=True, blank=True)

    class Meta(GenericMeta):
        object_class = OpeniFile
        resource_name = 'File'
