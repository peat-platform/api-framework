from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *
import os

class dropboxMedia(bcMedia):
    """ This class is used to:
        AUDIO MAPPING
        1.  Get a Dropbox audio
        2.  Get all Dropbox audios for an account
        3.  Post a audio to a simple account
        4.  Get all audios from an Dropbox album
        5.  Post a audio to an Dropbox album
        6.  Edit a audio 
        7.  Delete a audio
        
        FILE MAPPING
        8.  Get a Dropbox file
        9.  Get all Dropbox files for an account
        10.  Post a file to a simple account
        11.  Get all files from an Dropbox album
        12.  Post a file to an Dropbox album
        13.  Edit a file 
        14.  Delete a file
    
        PHOTO MAPPING
        15.  Get a Dropbox photo
        16.  Get all Dropbox photos for an account
        17. Post a photo to a simple account
        18. Get all photos from an Dropbox album
        19. Post a photo to an Dropbox album
        20. Edit a photo 
        21. Delete a photo
        
        VIDEO MAPPING
        22. Get a Dropbox video
        23. Get all Dropbox videos for an account
        24. Post a video to a simple account
        25. Get a video for an account
        26. Edit a video 
        27. Delete a video  
        
        FOLDER MAPPING
        28. Get a Dropbox folder
        29. Post a folder
        30. Delete a folder  
        
    """
    #   region Media API

    #   region Audio Object

    def get_an_audio(self, data):
        """ Get a audio by its id """
        # /audio_id (ie /cat.mp3 --> has to be the full filename, no ID) 
        f, metadata = self.connector.get_file_and_metadata('/' + data['audio_id'])
        account = self.connector.account_info()
        media = self.connector.media('/' + data['audio_id'])
                       
        raw_data = metadata
        if ('audio' in raw_data['mime_type']):
            names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
            names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
     
            fields = ['rev', '', 'service', '', '', '', '', '', 'created_time', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
     
            alternatives = ['', 'file', 'dropbox',  media['url'], account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     
            
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
        return "Not a Audio"
    
    def get_all_audios_for_account(self, data):
        """ Get all audios for an account """
        return {'result': 'Not applicable'}

    def post_audio_to_account(self, params):
        """ Post a audio to a simple account """
        if (check_if_exists(params, 'user_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                print "upload via source"
                f= open(self.params.path_string, 'rb')
                return self.connector.put_file(params['user_id'] +'/audios', f)
            elif (check_if_exists(params, 'url') != defJsonRes):
                print "upload via url"
                f= open(self.params.url, 'rb')
                return self.connector.put_file(params['user_id'] +'/audios', f)
        return "Insufficient Parameters"
    
    
    def get_all_audios_for_album(self, data):
        """ Get all audios for an album """
        metadata = self.connector.metadata('/' + params['album_id'])
        account = self.connector.account_info()
                       
        raw_datas = metadata
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
   
        fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
         
        alternatives = ['', 'file', 'dropbox', '', account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
         
        response = {
            'meta':
                {
                 'total_count': len(raw_datas['contents']),
                 'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                 'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
          
        for raw_data in raw_datas['contents']:
            print raw_data
            if not raw_data['is_dir']:
                if 'audio' in raw_data['mime_type']:
                    data = self.get_fields(raw_data, names, fields, alternatives)
                    response['data'].append(self.format_photo_response(data))
                              
        return response

    def post_audio_to_album(self, params):
        """ Post a audio to a simple account """
        if (check_if_exists(params, 'user_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                print "upload via source"
                f= open(self.params.path_string, 'rb')
                return self.connector.put_file(params['album_id'] +'/audios', f)
            elif (check_if_exists(params, 'url') != defJsonRes):
                print "upload via url"
                f= open(self.params.url, 'rb')
                return self.connector.put_file(params['album_id'] +'/audios', f)
        return "Insufficient Parameters"


    def edit_a_audio(self, data):
        """ Edit a audio object """
        return {'result': 'Not applicable'}

    def delete_a_audio(self, params):
        """ Delete a audio object """
        if (check_if_exists(params, 'audio_id') != defJsonRes):
            return self.connector.file_delete(params['audio_id'])
        return "Insufficient Parameters"


    #   endregion Connections

    #   endregion Audio Object
    
    #   region File Object

    def get_a_file(self, data):
        """ Get a file by its id """
        # /file_id (ie /cat.txt --> has to be the full filename, no ID) 
        f, metadata = self.connector.get_file_and_metadata('/' + data['file_id'])
        account = self.connector.account_info()
        media = self.connector.media('/' + data['file_id'])
                       
        raw_data = metadata
        print raw_data['mime_type']
        if ('text' in raw_data['mime_type']):
            names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
            names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
     
            fields = ['rev', '', 'service', '', '', '', '', '', 'created_time', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
     
            alternatives = ['', 'file', 'dropbox',  media['url'], account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     
            
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
        return "Not a File"
    
    def get_all_files_for_account(self, data):
        """ Get all files for an account """
        return {'result': 'Not applicable'}

    def post_file_to_account(self, params):
        """ Post a file to a simple account """
        if (check_if_exists(params, 'user_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                print "upload via source"
                f= open(self.params.path_string, 'rb')
                return self.connector.put_file(params['user_id'] +'/files', f)
            elif (check_if_exists(params, 'url') != defJsonRes):
                print "upload via url"
                f= open(self.params.url, 'rb')
                return self.connector.put_file(params['user_id'] +'/files', f)
        return "Insufficient Parameters"
    
    
    def get_all_files_for_album(self, data):
        """ Get all files for an album """
        metadata = self.connector.metadata('/' + params['album_id'])
        account = self.connector.account_info()
                       
        raw_datas = metadata
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
   
        fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
         
        alternatives = ['', 'file', 'dropbox', '', account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
         
        response = {
            'meta':
                {
                 'total_count': len(raw_datas['contents']),
                 'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                 'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
          
        for raw_data in raw_datas['contents']:
            print raw_data
            if not raw_data['is_dir']:
                if 'text' in raw_data['mime_type']:
                    data = self.get_fields(raw_data, names, fields, alternatives)
                    response['data'].append(self.format_photo_response(data))
                              
        return response

    def post_file_to_album(self, params):
        """ Post a file to a simple account """
        if (check_if_exists(params, 'user_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                print "upload via source"
                f= open(self.params.path_string, 'rb')
                return self.connector.put_file(params['album_id'] +'/files', f)
            elif (check_if_exists(params, 'url') != defJsonRes):
                print "upload via url"
                f= open(self.params.url, 'rb')
                return self.connector.put_file(params['album_id'] +'/files', f)
        return "Insufficient Parameters"


    def edit_a_file(self, data):
        """ Edit a file object """
        return {'result': 'Not applicable'}

    def delete_a_file(self, params):
        """ Delete a file object """
        if (check_if_exists(params, 'file_id') != defJsonRes):
            return self.connector.file_delete(params['file_id'])
        return "Insufficient Parameters"


    #   endregion Connections

    #   endregion File Object
    
    #   region Photo Object

    def get_a_photo(self, data):
        """ Get a photo by its id """
        # /photo_id (ie /cat.jpg --> has to be the full filename, no ID) 
        f, metadata = self.connector.get_file_and_metadata('/' + data['photo_id'])
        account = self.connector.account_info()
        media = self.connector.media('/' + data['photo_id'])
                       
        raw_data = metadata
        if ('image' in raw_data['mime_type']):
            names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
            names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
     
            fields = ['rev', '', 'service', '', '', '', '', '', 'created_time', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
     
            alternatives = ['', 'photo', 'dropbox',  media['url'], account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     
            
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
    
    def get_all_photos_for_account(self, params):
        """ Get all photos for an account """
        metadata = self.connector.metadata('/')
        account = self.connector.account_info()
                       
        raw_datas = metadata
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
   
        fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
         
        alternatives = ['', 'photo', 'dropbox', '', account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
         
        response = {
            'meta':
                {
                 'total_count': len(raw_datas['contents']),
                 'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                 'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
          
        for raw_data in raw_datas['contents']:
            if not raw_data['is_dir']:
                if 'image' in raw_data['mime_type']:
                    data = self.get_fields(raw_data, names, fields, alternatives)
                    response['data'].append(self.format_photo_response(data))
                              
        return response

    def post_photo_to_account(self, params):
        """ Post a photo to a simple account """
        if (check_if_exists(params, 'user_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                print "upload via source"
                f= open(self.params.path_string, 'rb')
                return self.connector.put_file('/', f)
            elif (check_if_exists(params, 'url') != defJsonRes):
                print "upload via url"
                f= open(self.params.url, 'rb')
                return self.connector.put_file('/', f)
        return "Insufficient Parameters"
    
    
    def get_all_photos_for_album(self, params):
        """ Get all photos for an album """
        metadata = self.connector.metadata('/' + params['album_id'])
        account = self.connector.account_info()
                       
        raw_datas = metadata
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
   
        fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
         
        alternatives = ['', 'photo', 'dropbox', '', account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
         
        response = {
            'meta':
                {
                 'total_count': len(raw_datas['contents']),
                 'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                 'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
          
        for raw_data in raw_datas['contents']:
            if not raw_data['is_dir']:
                if 'image' in raw_data['mime_type']:
                    data = self.get_fields(raw_data, names, fields, alternatives)
                    response['data'].append(self.format_photo_response(data))
                              
        return response


    def post_photo_to_album(self, params):
        """ Post a photo to a simple account """
        if (check_if_exists(params, 'album_id') != defJsonRes):
            if (check_if_exists(params, 'source') != defJsonRes):
                print "upload via source"
                f= open(params['source'], 'rb')
                return self.connector.put_file(params['album_id'], f)
            elif (check_if_exists(params, 'url') != defJsonRes):
                f= open(params['url'], 'rb')
                return self.connector.put_file(params['album_id'], f)
        return "Insufficient Parameters"


    def edit_a_photo(self, data):
        """ Edit a photo object """
        return {'result': 'Not applicable'}

    def delete_a_photo(self, params):
        """ Delete a photo object """
        if (check_if_exists(params, 'photo_id') != defJsonRes):
            return self.connector.file_delete(params['photo_id'])
        return "Insufficient Parameters"


    #   endregion Connections

    #   endregion Photo Object
    
    
    #   region Video Object

    def get_a_video(self, data):
        """ Get a video by its id """
        # /video_id (ie /cat.mov --> has to be the full filename, no ID) 
        f, metadata = self.connector.get_file_and_metadata('/' + data['video_id'])
        account = self.connector.account_info()
                       
        raw_data = metadata
        if ('video' in raw_data['mime_type']):
            names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
            names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
     
            fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
     
            alternatives = ['', 'video', 'dropbox',  media['url'], account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
     
            
            data = self.get_fields(raw_data, names, fields, alternatives)
            response = {
                        'meta':
                            {
                             'total_count': 1,
                             'next': None
                            },
                        'data': self.format_video_response(data)
                        }
                     
            return { 'response': response }
        return "Not a Video"
    
    def get_all_videos_for_account(self, data):
        """ Get all videos for an account """
        return {'result': 'Not applicable'}
    
    def get_all_videos_for_album(self, params):
        """ Get all videos for an album """
        metadata = self.connector.metadata('/' + params['album_id'])
        account = self.connector.account_info()
                       
        raw_datas = metadata
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
   
        fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
         
        alternatives = ['', 'video', 'dropbox', '', account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
         
        response = {
            'meta':
                {
                 'total_count': len(raw_datas['contents']),
                 'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                 'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
          
        for raw_data in raw_datas['contents']:
            if not raw_data['is_dir']:
                if 'video' in raw_data['mime_type']:
                    data = self.get_fields(raw_data, names, fields, alternatives)
                    response['data'].append(self.format_photo_response(data))
                              
        return response

    def post_video_to_account(self, params):
        """ Post a video to a simple account """
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
        """ Get all videos for an account """
        return {'result': 'Not applicable'}


    def edit_a_video(self, data):
        """ Edit a video object """
        return {'result': 'Not applicable'}

    def delete_a_video(self, params):
        """ Delete a video object """
        if (check_if_exists(params, 'video_id') != defJsonRes):
            return self.connector.file_delete(params['video_id'])
        return "Insufficient Parameters"


    #   endregion Connections

    #   endregion Video Object
    


    #   region Folder Aggregation 
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Folder%20Mapping

    def get_a_folder(self, params):
        """ GET API_PATH/[FOLDER_ID] """
        # /album_id (ie /10153665525255315)
        """ Get all folder for an album """
        metadata = self.connector.metadata('/' + params['album_id'])
        account = self.connector.account_info()
                       
        raw_datas = metadata
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
   
        fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
         
        alternatives = ['', 'album', 'dropbox', '', account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
         
        response = {
            'meta':
                {
                 'total_count': len(raw_datas['contents']),
                 'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                 'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
          
        for raw_data in raw_datas['contents']:
            data = self.get_fields(raw_data, names, fields, alternatives)
            response['data'].append(self.format_photo_response(data))
                              
        return response
    
    def post_folder_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID] """
        if (check_if_exists(params, 'folder_id') != defJsonRes):
            return self.connector.file_create_folder(params['folder_id'])
        return "Insufficient Parameters"

    def delete_a_folder(self, params):
        """ DELETE API_PATH/[FOLDER_ID] """
        if (check_if_exists(params, 'folder_id') != defJsonRes):
            return self.connector.file_delete(params['folder_id'])
        return "Insufficient Parameters"
    
    #   endregion Folder Aggregation

    #   endregion Media API