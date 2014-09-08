from OPENiapp.Providers.baseConnector import basicProvider
from _youtubemedia import youtubeMedia

import httplib2
import os
import sys

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client import tools
from oauth2client.tools import argparser
from oauth2client.tools import run

from _ytactivity import ytActivity
from _ytlocation import ytLocation
from _ytmedia import ytMedia
from _ytproductsServices import ytProductsServices
from _ytprofiles import ytProfiles

class provider(basicProvider, ytActivity, ytLocation, ytMedia, ytProductsServices, ytProfiles):
    """ This class is used to:
        1. Make the connection to the youtube
    """
    def __init__(self):#, data):
        """ Initiate the graph and find the OPENi album """
        #Link to client_secrets.json --> Created at https://console.developers.google.com/project/apps~{YOUR-APP}/apiui/credential --> Client ID for native application
        CLIENT_SECRETS_FILE = "client_secrets.json"
        
        # Helpful message to display if the CLIENT_SECRETS_FILE is missing.
        MISSING_CLIENT_SECRETS_MESSAGE = """
        WARNING: Please configure OAuth 2.0
        
        To make this sample run you will need to populate the client_secrets.json file
        found at:
        
           %s
        
        with information from the APIs Console
        https://code.google.com/apis/console#access
        
        For more information about the client_secrets.json file format, please visit:
        https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
        """ % os.path.abspath(os.path.join(os.path.dirname(__file__), CLIENT_SECRETS_FILE))
        
        flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
          message=MISSING_CLIENT_SECRETS_MESSAGE,
          scope='https://www.googleapis.com/auth/youtube')
        
        storage = Storage("%s-oauth2.json" % sys.argv[0])
        credentials = storage.get()
        
        if credentials is None or credentials.invalid:
          credentials = run(flow, storage)
        
        self.connector = build('youtube', 'v3', http=credentials.authorize(httplib2.Http()))
