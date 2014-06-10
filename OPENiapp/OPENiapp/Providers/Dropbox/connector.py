from dropbox import client, rest, session
from OPENiapp.Providers.baseConnector import basicProvider

# Include the Dropbox SDK
import dropbox


class provider(basicProvider):
    """ This class is used to:
        1. Make the connection to the dropbox
        2. Get user's photos, videos, audio, text files, documents and eBooks
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    """

    def __init__(self, application, access_token):#, data):
        """ Initiate the graph and find the OPENi album """
        self.connector = dropbox.client.DropboxClient(access_token)

#NEW STUFF NOT TESTED
    #   region Media API
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Media_API
    
    
    #   region Photo Object
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Photo_Mapping
    
    def get_a_photo(self, data):
        ''' GET API_PATH/[PHOTO_ID] '''
        # /media/media-id (ie media/628147512937366504_917877895)
        raw_data = self.connector.metadata(data['media_id'])
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': [self.format_photo_response(
                                        raw_data.contents.rev,
                                        self.check_if_exists(raw_data.contents, 'mime_type', 'image'),
                                        'openi',
                                        raw_data.contents.path,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.check_if_exists(raw_data.contents, 'photo-info', 'lat_long'),
                                        self.check_if_exists(raw_data.contents, 'photo-info', 'time_taken'),
                                        raw_data.contents.modified,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes
                                        )]
                    }
        return { 'response': response }

    def get_all_photos_for_account(self, data):
        ''' GET API_PATH/[ACCOUNT_ID]/photos '''
        # /users/user-id (ie users/917877895)
        raw_datas, next = self.connector.user_recent_media(data['account_id'])
        response = {
                    'meta': 
                        {
                        'total_count': len(raw_datas),
                        'next': next
                        },
                    'data' : [] }
        for raw_data in raw_datas:
            response['data'].append(self.format_photo_response(
                                        raw_data.contents.rev,
                                        self.check_if_exists(raw_data.contents, 'mime_type', 'image'),
                                        'openi',
                                        raw_data.contents.path,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.check_if_exists(raw_data.contents, 'photo-info', 'lat_long'),
                                        self.check_if_exists(raw_data.contents, 'photo-info', 'time_taken'),
                                        raw_data.contents.modified,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes
                                         ))
        return { 'response': response }
    
    #   region Video Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Video%20Mapping/
    #TODO add to baseConnector.py video stuff

    
    def get_a_video(self, data):
        ''' GET API_PATH/[PHOTO_ID] '''
        # /media/media-id (ie media/628147512937366504_917877895)
        raw_data = self.connector.metadata(data['media_id'])
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'next': None
                        },
                    'data': [self.format_video_response(
                                        raw_data.contents.rev,
                                        self.check_if_exists(raw_data.contents, 'mime_type', 'image'),
                                        'openi',
                                        raw_data.contents.path,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.check_if_exists(raw_data.contents, 'photo-info', 'lat_long'),
                                        self.check_if_exists(raw_data.contents, 'photo-info', 'time_taken'),
                                        raw_data.contents.modified,
                                        self.defJsonRes,
                                        self.defJsonRes,
                                        self.defJsonRes
                                        )]
                    }
        return { 'response': response }
        
    #   region Audio Object
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/Audio_Mapping
        #TODO add to baseConnector.py audio stuff
        
    #   region File Object
    #   As described here: http://redmine.openi-ict.eu/projects/openi/wiki/File_Mapping
        #TODO add to baseConnector.py file stuff
