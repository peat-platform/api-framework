from allauth.socialaccount.models import SocialAccount
from OPENiapp.Providers.base.profiles import bcProfiles
from OPENiapp.Providers.base.common import *

class goProfiles(bcProfiles):
    """ This class is used to:
        1. Get an Account
    """
    #   region Profiles API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Profiles%20API/

    def get_account(self):
        """ GET API_PATH/[EVENT_ID] """
        user = SocialAccount.objects.filter(provider="google")[0].user
        raw_data = SocialAccount.objects.filter(user=user)[0].extra_data

        names = ['id', 'object_type', 'service', 'resource_uri', 'from_id', 'from_object_type', 'from_resource_uri', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['person_name', 'person_surname', 'person_middlename', 'person_birthdate'])
        names.extend(['wallet_cards', 'wallet_name', 'wallet_description',
                      'wallet_id', 'wallet_object_type', 'wallet_service', 'wallet_url', 'wallet_from_id', 'wallet_from_object_type', 'wallet_from_url', 'wallet_from_name', 'wallet_time_created_time', 'wallet_time_edited_time', 'wallet_time_deleted_time'])
        names.extend(['user', 'username', 'email', 'password', 'validated', 'active'])

        fields = ['id', 'object_type', 'service', 'link', 'owner.id', 'owner.category', 'owner.url', 'owner.name', 'time.created_time', 'time.edited_time', 'time.deleted_time']
        fields.extend(['person_name', 'person_surname', 'person_middlename', 'person_birthdate'])
        fields.extend(['wallet_cards', 'wallet_name', 'wallet_description',
                      'wallet_id', 'wallet_object_type', 'wallet_service', 'wallet_url', 'wallet_from_id', 'wallet_from_object_type', 'wallet_from_url', 'wallet_from_name', 'wallet_time_created_time', 'wallet_time_edited_time', 'wallet_time_deleted_time'])
        fields.extend(['user', 'name', 'email', 'password', 'validated', 'active'])

        alternatives = ['', 'account', 'google', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', '', ''])
        alternatives.extend(['', '', '', '', '', '', '', '', '', '', '', '', '', ''])
        alternatives.extend(['', '', '', '', '', ''])
        
        data = self.get_fields(raw_data, names, fields, alternatives)

        response = {
            'meta': {
                'limit': self.check_if_exists(raw_datas, 'limit', None),
                'next': self.check_if_exists(raw_datas, 'paging.next', None),
                'offset': self.check_if_exists(raw_datas, 'offset', 0),
                'previous': self.check_if_exists(raw_datas, 'paging.previous', None),
                'total_count': self.check_if_exists(raw_datas, 'total_count', 1)
            },
            'objects': [self.format_account_response(data)]
        }
        
        return response
    
    #   endregion Profiles API