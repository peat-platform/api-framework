from OPENiapp.Providers.baseConnector import basicProvider

from provider import citygridplaces
# https://github.com/CityGrid/CityGrid-Python-Samples/blob/master/class-citygrid-places-api.py

from _cgactivity import cgActivity
from _cglocation import cgLocation
from _cgmedia import cgMedia
from _cgproductsServices import cgProductsServices
from _cgprofiles import cgProfiles

class provider(basicProvider, cgActivity, cgLocation, cgMedia, cgProductsServices, cgProfiles):
    ''' This class is used to:
        1. Make the connection to the Citygrid API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    '''
    def __init__(self):
        ''' Initiate the connector '''
        self.connector = citygridplaces()