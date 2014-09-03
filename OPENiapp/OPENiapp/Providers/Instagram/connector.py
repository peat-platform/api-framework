from instagram.client import InstagramAPI
import httplib2
import simplejson
from OPENiapp.Providers.baseConnector import basicProvider
from _inextra import inExtra
from _inmedia import inMedia

class provider(basicProvider, inExtra, inMedia):
    ''' This class is used to:
        1. Make the connection to the Instagram API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    '''
    def __init__(self, access_token):
        ''' Initiate the connector '''
        self.connector = InstagramAPI(access_token=access_token)