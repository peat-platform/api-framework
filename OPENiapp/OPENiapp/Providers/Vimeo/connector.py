# Include the Dropbox SDK
from vimeo import VimeoClient
#from dropbox import client, rest, session
from OPENiapp.Providers.baseConnector import basicProvider

from _vimeoactivity import vimeoActivity
from _vimeolocation import vimeoLocation
from _vimeomedia import vimeoMedia
from _vimeoproductsServices import vimeoProductsServices
from _vimeoprofiles import vimeoProfiles

class provider(basicProvider, vimeoActivity, vimeoLocation, vimeoMedia, vimeoProductsServices, vimeoProfiles):
    """ This class is used to:
        1. Make the connection to the vimeo
    """
    def __init__(self, access_token):#, data):
        """ Initiate the graph and find the OPENi album """
        self.connector = VimeoClient(access_token=access_token)
        