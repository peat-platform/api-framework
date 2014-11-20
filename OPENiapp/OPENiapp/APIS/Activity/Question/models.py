from django.db import models
from OPENiapp.APIS.models import *

from OPENiapp.APIS.Secondary.QuestionOption.models import OpeniQuestionOption


class OpeniQuestion(OpeniContextAwareModel):
    # id is missing because it is the default
    question = models.TextField()
    options = models.ForeignKey(OpeniQuestionOption)