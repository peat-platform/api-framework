from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *

class dropboxmedia(bcMedia):
    """ This class is used to:
        1. Make the connection to the Dropbox connector API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    """
    #   region Media API
    
    #   region Photo Object

    def get_a_photo(self, data):
        """ Get a photo by its id """
        # /photo_id (ie /10153665526210315)
        raw_data = self.connector.get('/' + data['photo_id'])


        names = ['id', 'object_type', 'service', 'url', 'file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'from_id', 'from_name', 'from_surname', 'from_middlename', 'from_birthdate', 'from_organizations', 'location_latitude', 'location_longtitude', 'location_height', 'tags', 'created_time', 'edited_time', 'deleted_time', 'height', 'width']

        fields = ['id', 'object_type', 'service', 'link', 'name', 'description', 'format', 'size', 'icon', 'from.id', 'from.name', 'from.surname', 'from.middlename', 'from.birthdate', 'from.organizations', 'place.location.latitude', 'place.location.longtitude', 'place.location.height', 'tags.data', 'created_time', 'updated_time', 'deleted_time', 'height', 'width']

        alternatives = ['', 'album', 'dropbox', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': self.format_photo_response(data)
                    }

        # Curate tag array from Dropbox
        tag_array = []
        for tag in raw_data['tags']['data']:
            tag_array.append(format_tags(tag['id'], tag['name'], tag['created_time'], '', '', tag['x'], tag['y']))
        response['data']['tags'] = tag_array
        
        return { 'response': response }
    
    def get_all_photos_for_account(self, data):
        """ Get all photos for an account """
        return self.connector.get(self.data.user_id+'/photos')

    def post_photo_to_account(self, data):
        """ Post a photo to a simple account """
        return self.connector.post(path = self.data.user_id+'/photos', source = open(self.data.path_string, 'rb'))


    def edit_photo_object(self, data):
        """ Edit a photo object """
        return {'result': 'Not applicable'}

    def delete_photo_object(self, data):
        """ Delete a photo object """
        return self.connector.delete(self.data.photo_id)


    #   endregion Connections

    #   endregion Photo Object
    


    #   region Folder Aggregation 
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Folder%20Mapping

    def get_a_folder(self, data):
        """ GET API_PATH/[FOLDER_ID] """
        # /album_id (ie /10153665525255315)
        raw_data = self.connector.get('/' + data['album_id'])
        raw_data2 = self.connector.get('/' + data['album_id'] + '/photos')

        names = ['id', 'object_type', 'service', 'url', 'file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'from_id', 'from_name', 'from_surname', 'from_middlename', 'from_birthdate', 'from_organizations', 'created_time', 'edited_time', 'deleted_time', 'data']
        fields = ['id', 'object_type', 'service', 'link', 'name', 'description', 'format', 'size', 'icon', 'from.id', 'from.name', 'from.surname', 'from.middlename', 'from.birthdate', 'from.organizations', 'created_time', 'updated_time', 'deleted_time', 'data']
        alternatives = ['', 'album', 'facebook', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

        data = self.get_fields(raw_data, names, fields, alternatives)
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': self.format_folder_response(data)
                    }
        return { 'response': response }

    #   endregion Folder Aggregation

    #   endregion Media API