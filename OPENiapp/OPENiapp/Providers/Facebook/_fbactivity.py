from OPENiapp.Providers.base.activity import bcActivity
from OPENiapp.Providers.base.common import *

class fbActivity(bcActivity):
    """ This class is used to:
        0.5 Get a Facebook Checkin

        1. Get a Facebook Event
        2. Get all Events for a Facebook Account

        3. Get a Status
        4. Get all Statuses for an Account
        5. Post Status to Account
        6. Post Status to Aggregation
        7. Delete a Status

        8. Get all Comments for a Status
        9. Post a Comment to a Status
        10. Get all Likes for a Status
        11. Post a Like to a Status
        12. Post an Unlike to a Status

        13. Delete a Comment

        14. Get all Comments for a Checkin

        15. Get all RSVP for an Event
        16. Post an RSVP to an Event
    """
    #   region Activity API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Activity_API
    
    #   region Checkin Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Event_Mapping
    
    def get_checkin(self, id):
        """ GET API_PATH/[CHECKIN_ID] """
        # /checkin_id (ie /577733618968497)
        # It must be a post_id and from there we get the place if it exists
        raw_data = self.connector.get(id)
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['place_name', 'place_description', 'place_category', 'place_picture', 'place_address_street', 'place_address_number', 'place_address_apartment', 'place_address_city', 'place_address_locality', 'place_address_country', 'place_address_zip', 'place_location_latitude', 'place_location_longitude', 'place_location_height'])
        names.extend(['text'])

        fields = ['id', 'object_type', 'service', 'link', 'from.id', 'from.category', 'from.url', 'from.name', 'created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['place.name', '', '', '', '', '', '', 'place.location.city', '', 'place.location.country', '', 'place.location.latitude', 'place.location.longitude', ''])
        fields.extend(['name'])

        alternatives = ['', 'checkin', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', '', '', '', '', '', '', '', '', '', '', '', ''])
        alternatives.extend([''])

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'data': [self.format_checkin_response(data)]
                    }

        place_id = self.check_if_exists(raw_data, 'place.id')
        if (place_id != defJsonRes):
            raw_data2 = self.connector.get(place_id)
            response['data'][0]['place']['category'] = self.check_if_exists(raw_data2, 'category')
            response['data'][0]['place']['description'] = self.check_if_exists(raw_data2, 'description')
            response['data'][0]['place']['address']['street'] = self.check_if_exists(raw_data2, 'location.street')
            response['data'][0]['place']['address']['zip'] = self.check_if_exists(raw_data2, 'location.zip')

        return response
    
    #   region Connections


    #   endregion Connections

    #   endregion Checkin Object
    
    #   region Event Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Event_Mapping
    
    def get_event(self, id):
        """ GET API_PATH/[EVENT_ID] """
        # /event_id (ie /577733618968497)
        raw_data = self.connector.get(id)
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['place_name', 'place_description', 'place_category', 'place_picture', 'place_address_street', 'place_address_number', 'place_address_apartment', 'place_address_city', 'place_address_locality', 'place_address_country', 'place_address_zip', 'place_location_latitude', 'place_location_longitude', 'place_location_height'])
        names.extend(['duration_starts_time', 'duration_ends_time'])
        names.extend(['description', 'picture', 'title'])

        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['location', '', '', '', '', '', '', '', '', '', '', 'venue.latitude', 'venue.longitude', ''])
        fields.extend(['start_time', 'end_time'])
        fields.extend(['description', 'picture', 'name'])

        alternatives = ['', 'event', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', '', '', '', '', '', '', '', '', '', '', '', ''])
        alternatives.extend(['', ''])
        alternatives.extend(['', '', ''])

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

    def get_events(self, id):
        return self.get_account_events('me')

    def get_account_events(self, id):
        """ GET API_PATH/[ACCOUNT_ID]/events """
        # /account_id/events (ie /675350314/events)
        raw_datas = self.connector.get('/' + id + '/events')
        
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

    def get_status(self, id):
        """ GET API_PATH/{STATUS_ID} """
        # /status_id (ie /10154016839520315)
        raw_data = self.connector.get('/' + id)
        
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
                    'data': [self.format_status_response(data)]
                    }
        return response

    def get_statuses(self, id):
        return self.get_account_statuses('me')

    def get_account_statuses(self, id):
        """ GET API_PATH/[ACCOUNT_ID]/STATUSES """
        # /account_id/statuses (ie /675350314/statuses)
        raw_datas = self.connector.get('/' + id + '/statuses')
        
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
    
    def post_statuses(self, id, params):
        return self.post_account_statuses('me', params)

    def post_account_statuses(self, id, params):
        """ POST API_PATH/[ACCOUNT_ID]/feed """
        # /account_id/feed (ie /675350314/feed)
        if (id):
            if (check_if_exists(params, 'message') != defJsonRes):
                return self.connector.post(path = id +'/feed', message = params['message'])
        return "Insufficient Parameters"

    # Not exposed currently
    def post_aggregation_statuses(self, id, params):
        """ POST API_PATH/{AGGREGATION_ID}/feed """
        # /aggregation_id/feed (ie /sth/feed)
        if (id):
            if (check_if_exists(params, 'message') != defJsonRes):
                return self.connector.post(path = id +'/feed', message = params['message'])
            #if (check_if_exists(params, 'page_id') != defJsonRes):
            #    return self.connector.post(path = params['page_id'] +'/feed', message = params['message'])
            #elif (check_if_exists(params, 'event_id') != defJsonRes):
            #    return self.connector.post(path = params['event_id'] +'/feed', message = params['message'])
            #elif (check_if_exists(params, 'group_id') != defJsonRes):
            #    return self.connector.post(path = params['group_id'] +'/feed', message = params['message'])
        return "Insufficient Parameters"

    def delete_status(self, id):
        """ DELETE API_PATH/{STATUS_ID} """
        # /status_id (ie /10154016839520315)
        return self.connector.delete(id)
    
    #   region Connections

    def get_status_comments(self, id):
        """ GET API_PATH/[STATUS_ID]/comments """
        # /status_id/comments (ie /10154016839520315/comments)
        raw_datas = self.connector.get('/' + id + '/comments')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['title', 'text', 'target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['title', 'text', 'target_id'])

        alternatives = ['', 'comment', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', params['status_id']])

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

    def post_status_comments(self, id, params):
        """ POST API_PATH/[STATUS_ID]/comments """
        # /status_id/comments (ie /10154016839520315/comments)
        if (id):
            if (check_if_exists(params, 'text') != defJsonRes):
                return self.connector.post(path = id +'/comments', message = params['text'])
            elif (check_if_exists(params, 'attachment_id') != defJsonRes):
                return self.connector.post(path = id +'/comments', attachment_id = params['attachment_id'])
            elif (check_if_exists(params, 'attachment_url') != defJsonRes):
                return self.connector.post(path = id +'/comments', attachment_url = params['attachment_url'])
            elif (check_if_exists(params, 'source') != defJsonRes):
                return self.connector.post(path = id +'/comments', source = params['source'])
        return "Insufficient Parameters"

    def post_status_likes(self, id):
        """ POST API_PATH/[STATUS_ID]/likes """
        # /status_id/likes (ie /10154016839520315/likes)
        return self.connector.post(path = id +'/likes')

    def get_status_likes(self, id):
        """ GET API_PATH/[STATUS_ID]/likes """
        # /status_id/likes (ie /10154016839520315/likes)
        raw_datas = self.connector.get('/' + id + '/likes')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['target_id'])

        alternatives = ['', 'like', 'facebook', '', '', '', '', '', '', '', '']
        alternatives.extend([params['status_id']])

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

    def delete_status_likes(self, id):
        """ DELETE API_PATH/[STATUS_ID]/likes """
        # /status_id/likes (ie /10154016839520315/likes)
        return self.connector.delete(path = id +'/likes')

    #   endregion Connections
    
    #   endregion Status Object

    
    #   region Secondary Objects

    #   region Comment Object

    def delete_comment(self, id):
        """ DELETE API_PATH/[COMMENT_ID] """
        # /comment_id (ie /10154016839520315_49048872)
        response = self.connector.delete('/' + id)
        return response

    #   Checkins

    def get_checkin_comments(self, id):
        """ GET API_PATH/[CHECKIN_ID]/comments """
        # /checkin_id/comments (ie /675350314_10154201196440315/comments)
        raw_datas = self.connector.get('/' + id + '/comments')

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

    #   region rsvp Object

    def get_event_rsvp(self, id):
        """ GET API_PATH/[EVENT_ID]/attending """
        # /event_id/attending (ie /577733618968497/attending)
        raw_datas = self.connector.get('/' + id + '/attending')

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['rsvp', 'target_id'])

        fields = ['id', 'object_type', 'service', 'link', 'id', 'category', 'url', 'name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['rsvp_status', 'id'])

        alternatives = ['', 'rsvp', 'facebook', '', '', '', '', '', '', '', '']
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
            response['data'].append(self.format_rsvp_response(data))
        return response

    def post_event_rsvp(self, id, params):
        """ POST API_PATH/[EVENT_ID]/attending """
        # /event_id/attending (ie /577733618968497/attending)
        if (check_if_exists(params, 'rsvp') != defJsonRes):
            return self.connector.post('/' + id + '/' + params['rsvp'])
        return "Insufficient Parameters"

    #   endregion rsvp Object

    #   endregion Secondary Objects

    #   endregion Activity API