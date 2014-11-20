__author__ = 'mpetyx'

from .models import OpeniNote

from OPENiapp.APIS.OpeniGenericResource import GenericMeta
from OPENiapp.APIS.OPENIResource import OpeniResource


class NoteResource(OpeniResource):
    class Meta(GenericMeta):
        queryset = OpeniNote.objects.all()
        resource_name = 'Note'
        extra_actions = [
            {
                "name": "",
                "http_method": "PUT",
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
            {
                "name": "",
                "http_method": "GET",
                "summary": "",
                "resource_type": "list",
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
            {
                "name": "",
                "http_method": "POST",
                "summary": "",
                "resource_type": "list",
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
            {
                "name": "",
                "http_method": "DELETE",
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
            {
                "name": "comments",
                "http_method": "GET",
                "summary": "Retrieve comments for a single openi note by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    }
                },
            },
            {
                "name": "comments",
                "http_method": "POST",
                "summary": "Create comment for a single openi note by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    },
                    "title": {
                        "type": "string",
                        "required": False,
                        "description": "title for the comment"
                    },
                    "text": {
                        "type": "string",
                        "required": False,
                        "description": "text of the comment"
                    }
                },
            },
            {
                "name": "likes",
                "http_method": "GET",
                "summary": "Retrieve likes for a single openi note by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    }
                },
            },
            {
                "name": "likes",
                "http_method": "POST",
                "summary": "Likes a note by id",
                "fields": {
                    "cbs": {
                        "type": "string",
                        "required": False,
                        "description": "OPENi"
                    },
                    "user": {
                        "type": "string",
                        "required": False,
                        "description": "Registered and authenicated user"
                    }
                },
            }
        ]