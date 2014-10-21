from OPENiapp.Providers.base.common import *

class foExtra():
    """ This class is used to:
        1. Retrieve all categories
        2. Search for venues
    """
    def search_category(self, params):
        return self.connector.venues.categories()

    def search_venues(self, params):
        # {"near": "Athens", "limit": "12", "radius": "800", "categoryId": "4bf58dd8d48988d116941735"}
        if (check_if_exists(params, 'categoryId') != defJsonRes):
            if (check_if_exists(params, 'll') != defJsonRes):
                if (check_if_exists(params, 'limit') != defJsonRes):
                    if (check_if_exists(params, 'radius') != defJsonRes):
                        raw = self.connector.venues.search(params={'categoryId': params['categoryId'], 'll': params['ll'], 'limit': params['limit'], 'radius': params['radius']})
                    else:
                        raw = self.connector.venues.search(params={'categoryId': params['categoryId'], 'll': params['ll'], 'limit': params['limit']})
                elif (check_if_exists(params, 'radius') != defJsonRes):
                    raw = self.connector.venues.search(params={'categoryId': params['categoryId'], 'll': params['ll'], 'radius': params['radius']})
                else:
                    raw = self.connector.venues.search(params={'categoryId': params['categoryId'], 'll': params['ll']})
                for idx, dato in enumerate(raw['venues']):
                    raw['venues'][idx]['photo'] = self.connector.venues.photos(dato['id'], params={})['photos']['items'][0]
                return raw

            elif (check_if_exists(params, 'near') != defJsonRes):
                if (check_if_exists(params, 'limit') != defJsonRes):
                    if (check_if_exists(params, 'radius') != defJsonRes):
                        raw = self.connector.venues.search(params={'categoryId': params['categoryId'], 'near': params['near'], 'limit': params['limit'], 'radius': params['radius']})
                    else:
                        raw = self.connector.venues.search(params={'categoryId': params['categoryId'], 'near': params['near'], 'limit': params['limit']})
                elif (check_if_exists(params, 'radius') != defJsonRes):
                    raw = self.connector.venues.search(params={'categoryId': params['categoryId'], 'near': params['near'], 'radius': params['radius']})
                else:
                    raw = self.connector.venues.search(params={'categoryId': params['categoryId'], 'near': params['near']})
                for idx, dato in enumerate(raw['venues']):
                    raw['venues'][idx]['photo'] = self.connector.venues.photos(dato['id'], params={})['photos']['items'][0]
                return raw

        return "Insufficient Parameters"

