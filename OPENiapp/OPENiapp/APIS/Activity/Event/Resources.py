from tastypie.authorization import DjangoAuthorization
from .models import OpeniEvent

from OPENiapp.APIS.OpeniGenericResource import GenericResource, GenericMeta

class EventResource(GenericResource):
    class Meta(GenericMeta):
<<<<<<< HEAD
        queryset = OpeniActivityEvent.objects.all()
        resource_name = 'Activityevent'
=======
        queryset = OpeniEvent.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'Event'
        authentication = Authentication()
        authorization = Authorization()
>>>>>>> FETCH_HEAD
