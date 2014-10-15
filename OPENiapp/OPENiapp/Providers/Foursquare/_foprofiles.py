from OPENiapp.Providers.base.profiles import bcProfiles
from OPENiapp.Providers.base.common import *

class foProfiles(bcProfiles):
    """ This class is used to:
        1. Get an Account
    """
    #   region Profiles API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Profiles%20API/

    def get_account(self):
        return get_an_account('self')
    
    def get_an_account(self, id):
        """ GET API_PATH/[ACCOUNT_ID] """
        raw_data = self.connector.users(id)

        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['person_name', 'person_surname', 'person_middlename', 'person_birthdate'])
        names.extend(['wallet_cards', 'wallet_name', 'wallet_description',
                      'wallet_id', 'wallet_object_type', 'wallet_service', 'wallet_url', 'wallet_from_id', 'wallet_from_object_type', 'wallet_from_url', 'wallet_from_name', 'wallet_time_created_time', 'wallet_time_edited_time', 'wallet_time_deleted_time'])
        names.extend(['user', 'username', 'email', 'password', 'validated', 'active'])

        fields = ['id', 'type', 'service', 'link', 'id', 'type', 'link', 'firstName', 'createdAt', 'time.updated_time', 'time.deleted_time']
        fields.extend(['firstName', 'lastName', '', ''])
        fields.extend(['wallet_cards', 'wallet_name', 'wallet_description',
                      'wallet_id', 'wallet_object_type', 'wallet_service', 'wallet_url', 'wallet_from_id', 'wallet_from_object_type', 'wallet_from_url', 'wallet_from_name', 'wallet_time_created_time', 'wallet_time_edited_time', 'wallet_time_deleted_time'])
        fields.extend(['user', 'username', 'email', 'password', 'verified', 'active'])

        alternatives = ['', 'account', 'foursquare', '', '', 'person', '', '', '', '', '']
        alternatives.extend(['', '', '', ''])
        alternatives.extend(['', '', '', '', '', '', '', '', '', '', '', '', '', ''])
        alternatives.extend(['', '', '', '', '', ''])
        
        data = self.get_fields(raw_data['user'], names, fields, alternatives)

        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': self.check_if_exists(raw_data, 'paging.previous'),
                         'next': self.check_if_exists(raw_data, 'paging.next')
                        },
                    'data': [self.format_account_response(data)]
                    }
        
        return response

    #   endregion Profiles API