__author__ = 'mpetyx'

from .models import OpeniStatus

from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.OPENIResource import OpeniResource


class StatusResource(OpeniResource):
    class Meta(GenericMeta):
        object_class = OpeniStatus
        resource_name = 'Status'
        extra_actions = [
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve a single cbs status by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:Facebook,Foursquare"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                }
            },
            {
                "name": "",
                "http_method": "DELETE",
                "summary": "Delete a Status",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "The CBS you want to make a call to"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    }
                }
            },
            {
                "name": "",
                "http_method": "GET",
                "summary": "Retrieve a list of cbs events",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:Facebook"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                },
                "resource_type": "list"
            },
            {
                "name": "like",
                "http_method": "GET",
                "summary": "Retrieve likes for a status by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:Facebook, OPENi"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                }
            },
            {
                "name": "comment",
                "http_method": "GET",
                "summary": "Retrieve comments for a status by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:Facebook, OPENi"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                }
            },
            {
                "name": "dislike",
                "http_method": "GET",
                "summary": "Retrieve dislikes for a status by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:OPENi"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                }
            },
            {
                "name": "favorite",
                "http_method": "GET",
                "summary": "Retrieve favorites for a status by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:OPENi"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                }
            },
            {
                "name": "comment",
                "http_method": "POST",
                "summary": "Post comment for a status by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:Facebook"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    },
                    "text": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook text"
                    },
                    "attachment_id": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook attachment_id"
                    },
                    "attachment_url": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook attachment_url"
                    },
                    "source": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook source"
                    },
                }
            },
            {
                "name": "like",
                "http_method": "POST",
                "summary": "Like a status by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:Facebook"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                }
            },
            {
                "name": "favorites",
                "http_method": "POST",
                "summary": "Favorite a status by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:Twitter"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                }
            },
            {
                "name": "",
                "http_method": "POST",
                "summary": "Post a status",
                "resource_type": "list",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:Twitter, Facebook"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "text": {
                        "type": "string",
                        "required": False,
                        "description": "Twitter text"
                    },
                    "message": {
                        "type": "string",
                        "required": False,
                        "description": "Facebook message"
                    }
                }
            },
            {
                "name": "like",
                "http_method": "DELETE",
                "summary": "Delete like for a status by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:Facebook, OPENi"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                }
            },
            {
                "name": "dislike",
                "http_method": "DELETE",
                "summary": "Delete dislike for a status by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:OPENi"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                }
            },
            {
                "name": "favorite",
                "http_method": "DELETE",
                "summary": "Delete favorite for a status by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "available:OPENi, Twitter"
                    },
                    "user": {
                        "type": "string",
                        "required": True,
                        "description": "Registered and authenicated user"
                    }
                }
            },
        ]




        #def prepend_urls(self):
        #    return [
        #        url(r"^(?P<resource_name>%s)/(?P<pk>\d+)/status%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_property'), name="status")
        #        ]