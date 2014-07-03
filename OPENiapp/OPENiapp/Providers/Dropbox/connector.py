# Include the Dropbox SDK
import dropbox
#from dropbox import client, rest, session
from OPENiapp.Providers.baseConnector import basicProvider
from _dropboxmedia import dropboxMedia

class provider(basicProvider, dropboxMedia):
    """ This class is used to:
        1. Make the connection to the dropbox
    """
    def __init__(self, application, access_token):#, data):
        """ Initiate the graph and find the OPENi album """
        # Get a DropboxClient object using an existing OAuth 1 access token.
        #hard coded key client_id and secret 
        sess = dropbox.session.DropboxSession('phqn3ej2gcpmzjj', 'txjz23vd9pfl3w6')
        sess.set_token(access_token[0].token, access_token[0].token_secret) 
        
        self.connector = dropbox.client.DropboxClient(sess)
        
        