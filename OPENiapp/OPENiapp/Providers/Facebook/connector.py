from facepy import GraphAPI
from OPENiapp.Providers.baseConnector import basicProvider
from _fbmedia import fbMedia
from _fbprofiles import fbProfiles
from _fbactivity import fbActivity

# For testing purposes go to https://developers.facebook.com/tools/explorer/ and play
class provider(basicProvider, fbMedia, fbProfiles, fbActivity):
    """ This class is used to:
        1. Make the connection to the Facebook Graph API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    """
    def __init__(self, application, access_token):#, data):
        """ Initiate the graph and find the OPENi album """
        self.connector = GraphAPI(access_token)

    

