__author__ = 'mpetyx'

from tastypie import fields

from .models import OpeniArticle
from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication
from OPENiapp.APIS.resources import TagsResource, BaseFileResource, DurationResource
from OPENiapp.APIS.OPENIResource import OpeniResource


class ArticleResource(OpeniResource):
    Duration = fields.ForeignKey(DurationResource, 'Duration', null=True, blank=True)
    BaseTag = fields.ForeignKey(TagsResource, 'BaseTag', null=True, blank=True)
    BaseFile = fields.ForeignKey(BaseFileResource, 'BaseFile', null=True, blank=True)

    class Meta(GenericMeta):
        object_class = OpeniArticle
        resource_name = 'Article'
