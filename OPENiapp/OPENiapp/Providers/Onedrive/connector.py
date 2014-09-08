# Include the Onedrive SDK
import onedrive
#from onedrive import client, rest, session
from OPENiapp.Providers.baseConnector import basicProvider

from _odactivity import odActivity
from _odlocation import odLocation
from _odmedia import odMedia
from _odproductsServices import odProductsServices
from _odprofiles import odProfiles

class provider(basicProvider, odActivity, odLocation, odMedia, odProductsServices, odProfiles):
    """ This class is used to:
        1. Make the connection to the onedrive
    """
    
    def __init__(self, access_token):#, data):
        """ Initiate the graph and find the OPENi album """
        print "access_token:" + access_token
        #self.connector = onedrive(access_token)
        api = api_v5.PersistentOneDriveAPI.from_conf(optz.config)
        api.auth_get_token(access_token)
        