from OPENiapp.Providers.base.activity import bcActivity
from OPENiapp.Providers.base.common import *

class goActivity(bcActivity):

    def get_checkin(self, id):
        """ GET API_PATH/[CHECKIN_ID] """
        # /reference (ie /CnRsAAAA98C4wD-VFvzGq-KHVEFhlHuy1TD1W6UYZw7KjuvfVsKMRZkbCVBVDxXFOOCM108n9PuJMJxeAxix3WB6B16c1p2bY1ZQyOrcu1d9247xQhUmPgYjN37JMo5QBsWipTsnoIZA9yAzA-0pnxFM6yAcDhIQbU0z05f3xD3m9NQnhEDjvBoUw-BdcocVpXzKFcnMXUpf-nkyF1w)
        return self.connector.checkin(id)