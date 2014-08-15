# Include the Onedrive SDK
import onedrive
#from onedrive import client, rest, session
from OPENiapp.Providers.baseConnector import basicProvider
from _onedrivemedia import onedriveMedia

class provider(basicProvider, onedriveMedia):
    """ This class is used to:
        1. Make the connection to the onedrive
    """
    
    def __init__(self, access_token):#, data):
        """ Initiate the graph and find the OPENi album """
        print "access_token:" + access_token
        #self.connector = onedrive(access_token)
        api = api_v5.PersistentOneDriveAPI.from_conf(optz.config)
        api.auth_get_token(access_token)
        