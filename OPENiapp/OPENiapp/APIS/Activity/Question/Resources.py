__author__ = 'mpetyx'

from .models import OpeniQuestion
from OPENiapp.APIS.Secondary.QuestionOption.Resources import QuestionOptionResource
from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta
from tastypie import fields

class QuestionResource(GenericResource):
    QuestionOption = fields.ForeignKey(QuestionOptionResource, 'QuestionOption', null=True, blank=True)
    class Meta(GenericMeta):
        queryset = OpeniQuestion.objects.all()
        resource_name = 'Question'

