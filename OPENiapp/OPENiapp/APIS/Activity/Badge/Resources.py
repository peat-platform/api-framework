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
        extra_actions = [
        #     {
        #         "name": "",
        #         "http_method": "PUT",
        #         "summary": "",
        #         "fields": {
        #             "user": {
        #                 "type": "string",
        #                 "required": False,
        #                 "description": "Registered and authenicated user"
        #             },
        #             "cbs": {
        #                 "type": "string",
        #                 "required": False,
        #                 "description": "OPENi"
        #             },
        #
        #         }
        #     },
        #     {
        #         "name": "",
        #         "http_method": "GET",
        #         "summary": "",
        #         "resource_type": "list",
        #         "fields": {
        #             "user": {
        #                 "type": "string",
        #                 "required": False,
        #                 "description": "Registered and authenicated user"
        #             },
        #             "cbs": {
        #                 "type": "string",
        #                 "required": False,
        #                 "description": "OPENi"
        #             },
        #
        #         }
        #     },
        #     {
        #         "name": "",
        #         "http_method": "POST",
        #         "summary": "",
        #         "resource_type": "list",
        #         "fields": {
        #             "user": {
        #                 "type": "string",
        #                 "required": False,
        #                 "description": "Registered and authenicated user"
        #             },
        #             "cbs": {
        #                 "type": "string",
        #                 "required": False,
        #                 "description": "OPENi"
        #             },
        #
        #         }
        #     },
        #     {
        #         "name": "",
        #         "http_method": "DELETE",
        #         "summary": "",
        #         "fields": {
        #             "user": {
        #                 "type": "string",
        #                 "required": False,
        #                 "description": "Registered and authenicated user"
        #             },
        #             "cbs": {
        #                 "type": "string",
        #                 "required": False,
        #                 "description": "OPENi"
        #             },
        #
        #         }
        #     },
        #
            {
                "name": "",
                "http_method": "GET",
                "summary": "",
                "fields": {
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },

                }
            },

        ]