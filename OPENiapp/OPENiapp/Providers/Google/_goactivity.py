from OPENiapp.Providers.base.activity import bcActivity
from OPENiapp.Providers.base.common import *

class goActivity(bcActivity):

    def get_an_event(self, params):
        """ GET API_PATH/[EVENT_ID] """
        return defaultMethodResponse