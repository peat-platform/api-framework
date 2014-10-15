from OPENiapp.Providers.base.activity import bcActivity
from OPENiapp.Providers.base.common import *

class twActivity(bcActivity):
    """ This class is used to:
        1. Get a Status
        2. Get all Statuses for an Account
        3. Post Status to Account
        4. Delete a Status

        5. Get Favorites for Account
        6. Post a Favorite to a Status
        7. Delete all Favorites from a Status
    """
    #   region Activity API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Activity_API
    
    #   region Status Object

    def get_status(self, id):
        """ GET API_PATH/{STATUS_ID} """
        # /statuses/show/ (ie /statuses/show/483539224545984500)
        raw_data = self.connector.show_status(id = id)
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text'])

        fields = ['id', 'object_type', 'service', 'entities.urls[0].url', 'user.id', 'user.category', 'user.url', 'user.name', 'created_at', 'updated_time', 'time.deleted_time']
        fields.extend(['title', 'text'])
        
        alternatives = ['', 'status', 'twitter', '', '', 'user', '', '', '', '', '']
        alternatives.extend(['', ''])

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'data': [self.format_status_response(data)]
                    }
        return response

    def get_statuses(self, id):
        return self.get_account_statuses('')

    def get_account_statuses(self, id):
        """ GET API_PATH/[ACCOUNT_ID]/STATUSES """
        # /statuses/user_timeline (ie statuses/user_timeline/10876852)
        raw_datas = self.connector.get_user_timeline(id = id)
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text'])

        fields = ['id', 'object_type', 'service', 'entities.urls[0].url', 'user.id', 'user.category', 'user.url', 'user.name', 'created_at', 'updated_time', 'time.deleted_time']
        fields.extend(['title', 'text'])
        
        alternatives = ['', 'status', 'twitter', '', '', 'user', '', '', '', '', '']
        alternatives.extend(['', ''])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_status_response(data))
        return response

    def post_statuses(self, id, params):
        return self.post_account_statuses('')

    def post_account_statuses(self, id, params):
        """ POST API_PATH/[ACCOUNT_ID]/feed """
        # /statuses/update (ie statuses/update/)
        # NOTE: ONLY FOR THE AUTHENTICATED USER!!!
        if (check_if_exists(params, 'text') != defJsonRes):
            return self.connector.post('statuses/update', params = { "status" : params['text'] })
        return "Insufficient Parameters"

    def delete_status(self, id):
        """ DELETE API_PATH/{STATUS_ID} """
        # statuses/destroy/status_id (ie statuses/destroy/483547228670537700)
        return self.connector.post('statuses/destroy', { "id" : id })
    
    #   endregion Status Object

    #   region Favorite Object

    def get_favorites(self, id):
        """ GET API_PATH/[USER_ID]/favorites """
        # /favorites/list (ie favorites/list/10876852)
        raw_datas = self.connector.get_favorites(id = id)
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['target_id'])

        fields = ['id', 'object_type', 'service', 'entities.urls[0].url', 'user.id', 'user.category', 'user.url', 'user.name', 'created_at', 'updated_time', 'time.deleted_time']
        fields.extend(['target_id'])
        
        alternatives = ['', 'status', 'twitter', '', '', 'user', '', '', '', '', '']
        alternatives.extend([''])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_favorite_response(data))
        return response

    def post_status_favorites(self, id):
        """ POST API_PATH/[STATUS_ID]/favorites """
        # /favorites/create/status_id (ie /favorites/create/458974978155614209)
        return self.connector.post('favorites/create', params = { "status_id" : id })

    def delete_status_favorites(self, id):
        """ DELETE API_PATH/[USER_ID]/favorites """
        # /favorites/destroy/status_id (ie /favorites/destroy/458974978155614209)
        return self.connector.post('favorites/destroy', params = { "status_id" : id })

    #   endregion Favorite Object

    #   endregion Secondary Objects

    #   endregion Activity API