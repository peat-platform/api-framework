__author__ = 'mpetyx'


from .models import OpeniArticle
from tastypie import fields
from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from OPENiapp.APIS.OPENiAuthorization import Authorization
from OPENiapp.APIS.OPENiAuthentication import Authentication
from OPENiapp.APIS.resources import TagsResource, BaseFileResource, DurationResource


class ArticleResource(GenericResource):
    Duration = fields.ForeignKey(DurationResource, 'Duration', null=True, blank=True)
    BaseTag = fields.ForeignKey(TagsResource, 'BaseTag', null=True, blank=True)
    BaseFile = fields.ForeignKey(BaseFileResource, 'BaseFile')
    class Meta(GenericMeta):
        queryset = OpeniArticle.objects.select_related("context").all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Article'
        authentication = Authentication()
        authorization = Authorization()
        # filtering = {
        #     'slug': ALL,
        #     'user': ALL_WITH_RELATIONS,
        #     'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        # }
