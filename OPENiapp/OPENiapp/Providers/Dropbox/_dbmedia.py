from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *
import os

class dbMedia(bcMedia):
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

    def get_audio(self, id):
        """ Get a audio by its id """
        # /audio_id (ie /cat.mp3 --> has to be the full filename, no ID) 
        f, metadata = self.connector.get_file_and_metadata('/' + id)
        account = self.connector.account_info()
        media = self.connector.media('/' + id)
                       
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

    def get_audios(self):
        return self.get_account_audios('me')
    
    def get_account_audios(self, id):
        """ Get all audios for an account """
        metadata = self.connector.metadata('/')
        account = self.connector.account_info()
                           
        raw_datas = metadata
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
       
        fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
             
        alternatives = ['', 'audio', 'dropbox', '', account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
             
        response = {
            'meta':
                {
                    'total_count': [],
                    'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                    'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
              
        i = 0
        for raw_data in raw_datas['contents']:
            if not raw_data['is_dir']:
                if 'audio' in raw_data['mime_type']:
                    data = self.get_fields(raw_data, names, fields, alternatives)
                    response['data'].append(self.format_photo_response(data)) 
                    i +=1
            else:
                dir_datas = self.connector.metadata(raw_data['path'])
                for dir_data in dir_datas['contents']:
                    if 'audio' in dir_data['mime_type']:
                        data = self.get_fields(dir_data, names, fields, alternatives)
                        response['data'].append(self.format_photo_response(data))   
                        i +=1
                            
        response['meta']['total_count'] = i                        
        return response

    def post_audios(self, params):
        return self.post_account_audio(self, 'me', params)

    def post_account_audio(self, id, params):
        """ Post a audio to a simple account """
        if (check_if_exists(params, 'source') != defJsonRes):
            f= open(params['source'], 'rb')
            return self.connector.put_file("/" + os.path.basename(params['source']), f)
        return "Insufficient Parameters"

    def delete_audio(self, id):
        """ Delete a audio object """
        return self.connector.file_delete(id)

    #   endregion Connections

    #   endregion Audio Object
    
    #   region File Object

    def get_file(self, id):
        """ Get a file by its id """
        # /file_id (ie /cat.txt --> has to be the full filename, no ID) 
        f, metadata = self.connector.get_file_and_metadata('/' + id)
        account = self.connector.account_info()
        media = self.connector.media('/' + id)
                       
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

    def get_files(self):
        return self.get_account_files('me')
    
    def get_account_files(self, id):
        """ Get all files for an account """
        metadata = self.connector.metadata('/')
        account = self.connector.account_info()
                           
        raw_datas = metadata
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
       
        fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
             
        alternatives = ['', 'files', 'dropbox', '', account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
             
        response = {
            'meta':
                {
                    'total_count': [],
                    'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                    'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
              
        i = 0
        for raw_data in raw_datas['contents']:
            if not raw_data['is_dir']:
                if 'text' in raw_data['mime_type']:
                    data = self.get_fields(raw_data, names, fields, alternatives)
                    response['data'].append(self.format_photo_response(data)) 
                    i +=1
            else:
                dir_datas = self.connector.metadata(raw_data['path'])
                for dir_data in dir_datas['contents']:
                    if 'text' in dir_data['mime_type']:
                        data = self.get_fields(dir_data, names, fields, alternatives)
                        response['data'].append(self.format_photo_response(data))   
                        i +=1
                            
        response['meta']['total_count'] = i                         
        return response

    def post_files(self, params):
        """ Post a file to a simple account """
        if (check_if_exists(params, 'source') != defJsonRes):
            f= open(params['source'], 'rb')
            return self.connector.put_file("/" + os.path.basename(params['source']), f)
        return "Insufficient Parameters"

    def delete_file(self, id):
        """ Delete a file object """
        return self.connector.file_delete(id)


    #   endregion Connections

    #   endregion File Object
    
    #   region Photo Object

    def get_photo(self, id):
        """ Get a photo by its id """
        # /photo_id (ie /cat.jpg --> has to be the full filename, no ID)
        f, metadata = self.connector.get_file_and_metadata('/' + id)
        account = self.connector.account_info()
        media = self.connector.media('/' + id)
               
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

    def get_photos(self):
        return self.get_account_photos('me')
    
    def get_account_photos(self, id):
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
                    'total_count': [],
                    'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                    'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
              
        i = 0
        for raw_data in raw_datas['contents']:
            if not raw_data['is_dir']:
                if 'image' in raw_data['mime_type']:
                    data = self.get_fields(raw_data, names, fields, alternatives)
                    response['data'].append(self.format_photo_response(data)) 
                    i +=1
            else:
                dir_datas = self.connector.metadata(raw_data['path'])
                for dir_data in dir_datas['contents']:
                    if 'image' in dir_data['mime_type']:
                        data = self.get_fields(dir_data, names, fields, alternatives)
                        response['data'].append(self.format_photo_response(data))   
                        i +=1
                            
        response['meta']['total_count'] = i                          
        return response

    def post_photos(self, params):
        """ Post a photo to a simple account """
        if (check_if_exists(params, 'source') != defJsonRes):
            f= open(params['source'], 'rb')
            return self.connector.put_file("/" + os.path.basename(params['source']), f)
        return "Insufficient Parameters"

    def delete_photo(self, id):
        """ Delete a photo object """
        return self.connector.file_delete(id)

    #   endregion Connections

    #   endregion Photo Object
    
    
    #   region Video Object

    def get_video(self, id):
        """ Get a video by its id """
        # /video_id (ie /cat.mov --> has to be the full filename, no ID) 
        f, metadata = self.connector.get_file_and_metadata('/' + id)
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

    def get_videos(self):
        return self.get_account_videos('me')
    
    def get_account_videos(self, id):
        """ Get all videos for an account """
        metadata = self.connector.metadata('/')
        account = self.connector.account_info()
                           
        raw_datas = metadata
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
       
        fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
             
        alternatives = ['', 'video', 'dropbox', '', account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
             
        response = {
            'meta':
                {
                    'total_count': [],
                    'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                    'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
              
        i = 0
        for raw_data in raw_datas['contents']:
            if not raw_data['is_dir']:
                if 'video' in raw_data['mime_type']:
                    data = self.get_fields(raw_data, names, fields, alternatives)
                    response['data'].append(self.format_photo_response(data)) 
                    i +=1
            else:
                dir_datas = self.connector.metadata(raw_data['path'])
                for dir_data in dir_datas['contents']:
                    if 'video' in dir_data['mime_type']:
                        data = self.get_fields(dir_data, names, fields, alternatives)
                        response['data'].append(self.format_photo_response(data))   
                        i +=1
                            
        response['meta']['total_count'] = i                          
        return response

    def post_videos(self, params):
        """ Post a video to a simple account """
        if (check_if_exists(params, 'source') != defJsonRes):
            f= open(params['source'], 'rb')
            return self.connector.put_file("/" + os.path.basename(params['source']), f)
        return "Insufficient Parameters"

    def delete_video(self, id):
        """ Delete a video object """
        return self.connector.file_delete(id)

    #   endregion Connections

    #   endregion Video Object
    

    #   region Folder Aggregation 

    def get_folder(self, id):
        """ GET API_PATH/[FOLDER_ID] """
        # /album_id (ie /10153665525255315)
        """ Get all folder for an album """
        metadata = self.connector.metadata('/' +id)
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

    def post_folders(self, params):
        """ POST API_PATH/[ACCOUNT_ID] """
        return self.connector.file_create_folder()

    def delete_folder(self, id):
        """ DELETE API_PATH/[FOLDER_ID] """
        return self.connector.file_delete(id)
    
    #   endregion Folder Aggregation

    #   region Album Aggregation
    
    def get_album_audios(self, id):
        """ Get all audios for an album """
        metadata = self.connector.metadata('/' + id)
        account = self.connector.account_info()
                       
        raw_datas = metadata
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
   
        fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
         
        alternatives = ['', 'audio', 'dropbox', '', account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
         
        response = {
            'meta':
                {
                 'total_count': [],
                 'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                 'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
         
        i = 0 
        for raw_data in raw_datas['contents']:
            print raw_data
            if not raw_data['is_dir']:
                if 'audio' in raw_data['mime_type']:
                    data = self.get_fields(raw_data, names, fields, alternatives)
                    response['data'].append(self.format_photo_response(data))
                    i += 1
        
        response['meta']['total_count'] = i                      
        return response

    def post_album_audios(self, id, params):
        """ Post a audio to a simple account """
        if (check_if_exists(params, 'source') != defJsonRes):
            f= open(params['source'], 'rb')
            return self.connector.put_file(id + "/" + os.path.basename(params['source']), f)
        return "Insufficient Parameters"
    
    def get_album_files(self, id):
        """ Get all files for an album """
        metadata = self.connector.metadata('/' + id)
        account = self.connector.account_info()
                       
        raw_datas = metadata
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
   
        fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
         
        alternatives = ['', 'file', 'dropbox', '', account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
         
        response = {
            'meta':
                {
                 'total_count': [],
                 'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                 'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
         
        i = 0 
        for raw_data in raw_datas['contents']:
            print raw_data
            if not raw_data['is_dir']:
                if 'text' in raw_data['mime_type']:
                    data = self.get_fields(raw_data, names, fields, alternatives)
                    response['data'].append(self.format_photo_response(data))
                    i += 1
        
        response['meta']['total_count'] = i                     
        return response

    def post_album_file(self, id, params):
        """ Post a file to a simple account """
        if (check_if_exists(params, 'source') != defJsonRes):
            f= open(params['source'], 'rb')
            return self.connector.put_file(id +"/" + os.path.basename(params['source']), f)
        return "Insufficient Parameters"

    def get_album_photos(self, id):
        """ Get all photos for an album """
        metadata = self.connector.metadata('/' + id)
        account = self.connector.account_info()
                       
        raw_datas = metadata
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
   
        fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
         
        alternatives = ['', 'photo', 'dropbox', '', account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
         
        response = {
            'meta':
                {
                 'total_count': [],
                 'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                 'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
         
        i = 0 
        for raw_data in raw_datas['contents']:
            print raw_data
            if not raw_data['is_dir']:
                if 'image' in raw_data['mime_type']:
                    data = self.get_fields(raw_data, names, fields, alternatives)
                    response['data'].append(self.format_photo_response(data))
                    i += 1
        
        response['meta']['total_count'] = i                       
        return response

    def post_album_photos(self, id, params):
        """ Post a photo to a simple account """
        if (check_if_exists(params, 'source') != defJsonRes):
            f= open(params['source'], 'rb')
            return self.connector.put_file(id +"/" + os.path.basename(params['source']), f)
        return "Insufficient Parameters"
    
    def get_album_videos(self, id):
        """ Get all videos for an album """
        metadata = self.connector.metadata('/' + id)
        account = self.connector.account_info()
                       
        raw_datas = metadata
        
        names = ['id', 'object_type', 'service', 'url', 'from_id', 'from_object_type', 'from_url', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon', 'location_latitude', 'location_longitude', 'location_height', 'tags', 'height', 'width'])
   
        fields = ['rev', '', 'service', 'path', '', '', '', '', 'modified', 'client_mtime', '', 'path', '', 'mime_type', 'size', 'icon', '', '', '', '', '', '']
         
        alternatives = ['', 'video', 'dropbox', '', account['uid'], '', account['referral_link'], account['display_name'], '', '', '', '', '', '', '', '', '', '', '', '', '', '']
         
        response = {
            'meta':
                {
                 'total_count': [],
                 'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                 'next': self.check_if_exists(raw_datas, 'paging.next')
                },
            'data': []
            }
         
        i = 0 
        for raw_data in raw_datas['contents']:
            print raw_data
            if not raw_data['is_dir']:
                if 'video' in raw_data['mime_type']:
                    data = self.get_fields(raw_data, names, fields, alternatives)
                    response['data'].append(self.format_photo_response(data))
                    i += 1
        
        response['meta']['total_count'] = i                      
        return response

    def post_album_videos(self, id, params):
        """ Post a photo to a simple account """
        if (check_if_exists(params, 'source') != defJsonRes):
            f= open(params['source'], 'rb')
            return self.connector.put_file(id +"/" + os.path.basename(params['source']), f)
        return "Insufficient Parameters"

    #   endregion Album Aggregation

    #   endregion Media API