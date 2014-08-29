from foursquare import Foursquare
from OPENiapp.Providers.baseConnector import basicProvider

from _fomedia import foMedia
from _foactivity import foActivity
from _foprofiles import foProfiles

class provider(basicProvider, foMedia, foActivity, foProfiles):
    ''' This class is used to:
        1. Make the connection to the Foursquare API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    '''
    def __init__(self, access_token):
        ''' Initiate the connector '''
        self.connector = Foursquare(access_token=access_token, version='20140116')