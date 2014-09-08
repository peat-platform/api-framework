from OPENiapp.Providers.baseConnector import basicProvider

import flickr_api
from flickr_api import test
API_KEY =  '64f368d7efc5406c1dbae3a0983cc607'
API_SECRET = 'a424445857273ee4'

from _flactivity import flActivity
from _fllocation import flLocation
from _flmedia import flMedia
from _flproductsServices import flProductsServices
from _flprofiles import flProfiles

class provider(basicProvider, flActivity, flLocation, flMedia, flProductsServices, flProfiles):
    ''' This class is used to:
        1. Make the connection to the Foursquare API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    '''
    def __init__(self):
        ''' Initiate the connector '''
        flickr_api.set_keys(api_key = API_KEY, api_secret = API_SECRET)
        a = flickr_api.auth.AuthHandler() #creates the AuthHandler object
        perms = "read, write" # set the required permissions
        url = a.get_authorization_url(perms)
        self.connector = flickr_api