from OPENiapp.Providers.base.activity import bcActivity
from OPENiapp.Providers.base.common import *

class fbActivity(bcActivity):
    """ This class is used to:
        1. Get a Facebook Event
        2. Get all Events for a Facebook Account
    """
    #   region Location API
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Location_API
    
    #   region Event Object
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Event_Mapping
    
    def get_an_event(self, params):
        """ GET API_PATH/[EVENT_ID] """
        # /event_id (ie /577733618968497)
        raw_data = self.connector.get(params['event_id'])
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['place_name', 'place_description', 'place_category', 'place_picture', 'place_address_street', 'place_address_number', 'place_address_apartment', 'place_address_city', 'place_address_locality', 'place_address_country', 'place_address_zip', 'place_location_latitude', 'place_location_longitude', 'place_location_height'])
        names.extend(['duration_starts_time', 'duration_ends_time'])
        names.extend(['description', 'picture', 'title'])

        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['location', '', '', '', '', '', '', '', '', '', '', 'venue.latitude', 'venue.longitude', '', 'start_time', 'end_time', 'description', 'picture', 'name'])

        alternatives = ['', 'event', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'data': [self.format_event_response(data)]
                    }
        return response

    def get_all_events_for_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/events """
        # /account_id/events (ie /675350314/events)
        raw_datas = self.connector.get('/' + params['user_id'] + '/events')
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['place_name', 'place_description', 'place_category', 'place_picture', 'place_address_street', 'place_address_number', 'place_address_apartment', 'place_address_city', 'place_address_locality', 'place_address_country', 'place_address_zip', 'place_location_latitude', 'place_location_longitude', 'place_location_height'])
        names.extend(['duration_starts_time', 'duration_ends_time'])
        names.extend(['description', 'picture', 'title'])

        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['location', '', '', '', '', '', '', '', '', '', '', 'venue.latitude', 'venue.longitude', '', 'start_time', 'end_time', 'description', 'picture', 'name'])
        
        alternatives = ['', 'event', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas['data']),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_event_response(data))
        return response
    
    #   region Connections


    #   endregion Connections

    #   endregion Event Object
    
    #   region Status Object

    def get_a_status(self, params):
        """ GET API_PATH/{STATUS_ID} """
        # /status_id (ie /10154016839520315)
        raw_data = self.connector.get('/' + params['status_id'])
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', 'from.category', 'from.url', 'from.name', 'time.created_time', 'updated_time', 'time.deleted_time']
        fields.extend(['title', 'message'])
        
        alternatives = ['', 'status', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', ''])

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'data': [self.format_event_response(data)]
                    }
        return response

    def get_all_statuses_for_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/STATUSES """
        # /account_id/statuses (ie /675350314/statuses)
        raw_datas = self.connector.get('/' + params['user_id'] + '/statuses')
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', 'from.category', 'from.url', 'from.name', 'time.created_time', 'updated_time', 'time.deleted_time']
        fields.extend(['title', 'message'])
        
        alternatives = ['', 'status', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', ''])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas['data']),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_status_response(data))
        return response

    def post_status_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/feed """
        # /account_id/feed (ie /675350314/feed)
        if (check_if_exists(params, 'user_id') != defJsonRes):
            if (check_if_exists(params, 'message') != defJsonRes):
                return self.connector.post(path = params['user_id'] +'/feed', message = params['message'])
        return "Insufficient Parameters"

    def post_status_to_aggregation(self, params):
        """ POST API_PATH/{AGGREGATION_ID}/feed """
        # /aggregation_id/feed (ie /sth/feed)
        if (check_if_exists(params, 'message') != defJsonRes):
            if (check_if_exists(params, 'page_id') != defJsonRes):
                return self.connector.post(path = params['page_id'] +'/feed', message = params['message'])
            elif (check_if_exists(params, 'event_id') != defJsonRes):
                return self.connector.post(path = params['event_id'] +'/feed', message = params['message'])
            elif (check_if_exists(params, 'group_id') != defJsonRes):
                return self.connector.post(path = params['group_id'] +'/feed', message = params['message'])
        return "Insufficient Parameters"

    def delete_a_status(self, params):
        """ DELETE API_PATH/{STATUS_ID} """
        # /status_id (ie /10154016839520315)
        if (check_if_exists(params, 'status_id') != defJsonRes):
            return self.connector.delete(params['status_id'])
        return "Insufficient Parameters"
    
    #   region Connections

    def get_status_comments(self, params):
        """ GET API_PATH/[STATUS_ID]/comments """
        # /status_id/comments (ie /10154016839520315/comments)
        raw_datas = self.connector.get('/' + params['status_id'] + '/comments')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text', 'target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['title', 'text', 'target_id'])

        alternatives = ['', 'comment', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', ''])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas['data']),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_comment_response(data))
        return response
        return defaultMethodResponse

    def __post_status_comment(self, params):
        return self.connector.post(path = params['status_id'] +'/comments',
                                    message = params['message'],
                                    attachment_id = params['attachment_id'],
                                    attachment_url = params['attachment_url'],
                                    source = open(params['source'], 'rb'))


    def post_status_comment(self, params):
        """ POST API_PATH/[STATUS_ID]/comments """
        # /status_id/comments (ie /10154016839520315/comments)
        if (check_if_exists(params, 'status_id') != defJsonRes):
            if (check_if_exists(params, 'message') != defJsonRes):
                return __post_status_comment(params)
            elif (check_if_exists(params, 'attachment_id') != defJsonRes):
                return __post_status_comment(params)
            elif (check_if_exists(params, 'attachment_url') != defJsonRes):
                return __post_status_comment(params)
            elif (check_if_exists(params, 'source') != defJsonRes):
                return __post_status_comment(params)
        return "Insufficient Parameters"

    def like_a_status(self, params):
        """ POST API_PATH/[STATUS_ID]/likes """
        # /status_id/likes (ie /10154016839520315/likes)
        if (check_if_exists(params, 'status_id') != defJsonRes):
            return self.connector.post(path = params['status_id'] +'/likes')
        return "Insufficient Parameters"

    def get_status_likes(self, params):
        """ GET API_PATH/[STATUS_ID]/likes """
        # /status_id/likes (ie /10154016839520315/likes)
        raw_datas = self.connector.get('/' + params['status_id'] + '/likes')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['target_id'])

        alternatives = ['', 'comment', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend([''])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas['data']),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_like_response(data))
        return response

    def unlike_status(self, params):
        """ DELETE API_PATH/[STATUS_ID]/likes """
        # /status_id/likes (ie /10154016839520315/likes)
        if (check_if_exists(params, 'status_id') != defJsonRes):
            return self.connector.delete(path = params['status_id'] +'/likes')
        return "Insufficient Parameters"

    #   endregion Connections
    
    #   endregion Status Object

    
    #   region Secondary Objects

    #   region Comment Object

    def delete_a_comment(self, params):
        """ DELETE API_PATH/[COMMENT_ID] """
        # /comment_id
        response = self.connector.delete(
            '/' + params['comment_id']
            )
        return response

    #   Checkins

    def get_comments_for_checkin(self, params):
        """ GET API_PATH/[POST_ID]/comments """
        # /post_id/comments (ie /675350314_10154201196440315/comments)
        raw_datas = self.connector.get('/' + params['post_id'] + '/comments')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text', 'target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['title', 'text', 'target_id'])

        alternatives = ['', 'comment', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', ''])

        response = {
                    'meta':
                        {
                            'total_count': len(raw_datas['data']),
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'data': []
                    }
        for raw_data in raw_datas['data']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_comment_response(data))
        return response

    #   endregion Comment Object

    #   endregion Secondary Objects

    #   endregion Location API