from common import *

class bcProfiles:
    #   region Profiles API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Profiles%20API/

    #   region Account Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/file/

    def format_account_response(self, params):
        response = {
                        "user": params['user'],
                        "username": params['username'],
                        "email": params['email'],
                        "password": params['password'],
                        "validated": params['validated'],
                        "active": params['active'],
                        "wallet": format_wallet(params),
                        "person": format_person(params)
                   }
        response.update(format_generic(params))
        return response

    def get_an_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID] """
        return defaultMethodResponse

    #   endregion Account Object

    #   endregion Profiles API