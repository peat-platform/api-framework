from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *
import os

class dropboxMedia(bcMedia):
    """ This class is used to:
        AUDIO MAPPING
        /
        
        FILE MAPPING
        1.  Get a Dropbox file
        2.  Get all Dropbox files for an account
        3.  Post a file to a simple account
        4.  Get all files from an Dropbox album
        5.  Post a file to an Dropbox album
        6.  Edit a file 
        7.  Delete a file
    
        PHOTO MAPPING
        8.  Get a Dropbox photo
        9.  Get all Dropbox photos for an account
        10. Post a photo to a simple account
        11. Get all photos from an Dropbox album
        12. Post a photo to an Dropbox album
        13. Edit a photo 
        14. Delete a photo
        
        VIDEO MAPPING
        15. Get a Dropbox video
        16. Get all Dropbox videos for an account
        17. Post a video to a simple account
        18. Post an video object to an aggregation
        19. Edit a video 
        20. Delete a video     
        
    """
    #   region Media API
    
    #   region Photo Object

    def get_a_photo(self, data):
        """ Get a photo by its id """
        # /photo_id (ie /cat.jpg --> has to be the full filename, no ID) 
        f, metadata = self.connector.get_file_and_metadata('/' + data['photo_id'])
                       
        raw_data = metadata
        print raw_data['mime_type']
        if ('image' in raw_data['mime_type']):
            names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
            names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
     
            fields = ['rev', 'mime_type', 'service', 'path', '', '', '', '', 'created_time', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
     
            alternatives = ['', 'photo', 'dropbox', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     
            
            data = self.get_fields(raw_data, names, fields, alternatives)
            response = {
                        'meta':
                            {
                             'total_count': 1,
                             'next': None
                            },
                        'data': self.format_photo_response(data)
                        }
                     
            return { 'response': response }
        return "Not a Photo"
    
    def get_all_photos_for_account(self, data):
        """ Get all photos for an account """
        return {'result': 'Not applicable'}

    def post_photo_to_account(self, params):
        """ Post a photo to a simple account """
        if (check_if_exists(params, 'user_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                print "upload via source"
                f= open(self.params.path_string, 'rb')
                return self.connector.put_file(params['user_id'] +'/photos', f)
            elif (check_if_exists(params, 'url') != defJsonRes):
                print "upload via url"
                f= open(self.params.url, 'rb')
                return self.connector.put_file(params['user_id'] +'/photos', f)
        return "Insufficient Parameters"
    
    
    def get_all_photos_for_album(self, data):
        """ Get all photos for an account """
        return {'result': 'Not applicable'}

    def post_photo_to_album(self, params):
        """ Post a photo to a simple account """
        if (check_if_exists(params, 'user_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                print "upload via source"
                f= open(self.params.path_string, 'rb')
                return self.connector.put_file(params['album_id'] +'/photos', f)
            elif (check_if_exists(params, 'url') != defJsonRes):
                print "upload via url"
                f= open(self.params.url, 'rb')
                return self.connector.put_file(params['album_id'] +'/photos', f)
        return "Insufficient Parameters"


    def edit_a_photo(self, data):
        """ Edit a photo object """
        return {'result': 'Not applicable'}

    def delete_a_photo(self, params):
        """ Delete a photo object """
        if (check_if_exists(params, 'video_id') != defJsonRes):
            return self.connector.file_delete(params['video_id'])
        return "Insufficient Parameters"


    #   endregion Connections

    #   endregion Photo Object
    
    
    #   region Video Object

    def get_a_video(self, data):
        """ Get a photo by its id """
        # /photo_id (ie /cat.jpg --> has to be the full filename, no ID) 
        f, metadata = self.connector.get_file_and_metadata('/' + data['video_id'])
                       
        raw_data = metadata
        print raw_data['mime_type']
        if ('video' in raw_data['mime_type']):
            names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
            names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
     
            fields = ['rev', 'mime_type', 'service', 'path', '', '', '', '', 'created_time', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
     
            alternatives = ['', 'video', 'dropbox', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     
            
            data = self.get_fields(raw_data, names, fields, alternatives)
            response = {
                        'meta':
                            {
                             'total_count': 1,
                             'next': None
                            },
                        'data': self.format_photo_response(data)
                        }
                     
            return { 'response': response }
        return "Not a Video"
    
    def get_all_videos_for_account(self, data):
        """ Get all photos for an account """
        return {'result': 'Not applicable'}

    def post_video_to_account(self, params):
        """ Post a photo to a simple account """
        if (check_if_exists(params, 'user_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                print "upload via source"
                f= open(self.params.path_string, 'rb')
                return self.connector.put_file(params['user_id'] +'/videos', f)
            elif (check_if_exists(params, 'url') != defJsonRes):
                print "upload via url"
                f= open(self.params.url, 'rb')
                return self.connector.put_file(params['user_id'] +'/videos', f)
        return "Insufficient Parameters"
    
    
    def post_video_to_aggregation(self, data):
        """ Get all photos for an account """
        return {'result': 'Not applicable'}


    def edit_a_video(self, data):
        """ Edit a photo object """
        return {'result': 'Not applicable'}

    def delete_a_video(self, params):
        """ Delete a photo object """
        if (check_if_exists(params, 'video_id') != defJsonRes):
            return self.connector.file_delete(params['video_id'])
        return "Insufficient Parameters"


    #   endregion Connections

    #   endregion Video Object
    


    #   region Folder Aggregation 
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Folder%20Mapping

    def get_a_folder(self, data):
        """ GET API_PATH/[FOLDER_ID] """
        # /album_id (ie /10153665525255315)
        metadata = self.connector.metadata('/' + data['folder_id'])
                       
        raw_data = metadata
        print raw_data
#         if ('folder' in raw_data['icon']):
#              names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
#              names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
#       
#              fields = ['rev', 'mime_type', 'service', 'path', '', '', '', '', 'created_time', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
#       
#              alternatives = ['', 'video', 'dropbox', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
#       
#              
#              data = self.get_fields(raw_data, names, fields, alternatives)
#              response = {
#                          'meta':
#                              {
#                               'total_count': 1,
#                               'next': None
#                              },
#                          'data': self.format_photo_response(data)
#                          }
#                       
#              return { 'response': response }
#         return "Not a Folder"
        return raw_data
    
    def post_folder_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID] """
        if (check_if_exists(params, 'folder_id') != defJsonRes):
            return self.connector.file_create_folder(params['folder_id'])
        return "Insufficient Parameters"

    def edit_a_folder(self, params):
        """ PUT API_PATH/[FOLDER_ID] """
        return defaultMethodResponse

    def delete_a_folder(self, params):
        """ DELETE API_PATH/[FOLDER_ID] """
        if (check_if_exists(params, 'folder_id') != defJsonRes):
            return self.connector.file_delete(params['folder_id'])
        return "Insufficient Parameters"
    
    #   endregion Folder Aggregation

    #   endregion Media API