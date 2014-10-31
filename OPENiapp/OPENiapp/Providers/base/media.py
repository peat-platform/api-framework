from common import *

class bcMedia:
    #   region Media API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Media%20API/

    #   region Audio Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/file/

    def format_audio_response(self, params):
        response = {
                        "file": format_file(params)
                   }
        response.update(format_generic(params))
        return response

    def get_audios(self):
        """ GET API_PATH/[ACCOUNT_ID]/audios """
        return defaultMethodResponse

    def post_audios(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/audio """
        return defaultMethodResponse
    
    def get_audio(self, id):
        """ GET API_PATH/[AUDIO_ID] """
        return defaultMethodResponse

    def put_audio(self, id, params):
        """ PUT API_PATH/[AUDIO_ID] """
        return defaultMethodResponse

    def delete_audio(self, id):
        """ DELETE API_PATH/[AUDIO_ID] """
        return defaultMethodResponse
    
    #   region Connections

    #   endregion AUDIO Object


    #   region File Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/file/

    def format_file_response(self, params):
        response = {
                        "file": format_file(params)
                   }
        response.update(format_generic(params))
        return response

    def get_files(self):
        """ GET API_PATH/[ACCOUNT_ID]/files """
        return defaultMethodResponse

    def post_files(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/files """
        return defaultMethodResponse
    
    def get_file(self, id):
        """ GET API_PATH/[FILE_ID] """
        return defaultMethodResponse

    def put_file(self, id, params):
        """ PUT API_PATH/[FILE_ID] """
        return defaultMethodResponse

    def delete_file(self, id):
        """ DELETE API_PATH/[FILE_ID] """
        return defaultMethodResponse
    
    #   region Connections

    #   endregion File Object

    
    #   region Photo Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/photo/

    def format_photo_response(self, params):
        response = {
                        "file": format_file(params),
                        "location": format_location(params),
                        "tags": params['tags'],
                        "height": params['height'],
                        "width": params['width']
                   }
        response.update(format_generic(params))
        return response

    def get_photos(self):
        """ GET API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse

    def post_photos(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse
    
    def get_photo(self, id):
        """ GET API_PATH/[PHOTO_ID] """
        return defaultMethodResponse

    def put_photo(self, id, params):
        """ PUT API_PATH/[PHOTO_ID] """
        return defaultMethodResponse

    def delete_photo(self, id):
        """ DELETE API_PATH/[PHOTO_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_photo_comments(self, id):
        """ GET API_PATH/[PHOTO_ID]/comments """
        return defaultMethodResponse

    def post_photo_comments(self, id, params):
        """ POST API_PATH/[PHOTO_ID]/comments """
        return defaultMethodResponse

    def get_photo_likes(self, id):
        """ GET API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def post_photo_likes(self, id, params):
        """ POST API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def delete_photo_likes(self, id, params):
        """ DELETE API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def get_photo_dislikes(self, id):
        """ GET API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse

    def post_photo_dislikes(self, id, params):
        """ POST API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse

    def delete_photo_dislikes(self, id):
        """ DELETE API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse


    #   endregion Connections

    #   endregion Photo Object
    
    #   region Video Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/video/

    def format_video_response(self, params):
        response = {
                        "file": format_file(params),
                        "location": format_location(params),
                        "duration": format_duration(params),
                        "tags": params['tags']
                   }
        response.update(format_generic(params))
        return response

    def get_videos(self):
        """ GET API_PATH/[ACCOUNT_ID]/videos """
        return defaultMethodResponse

    def post_videos(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/videos """
        return defaultMethodResponse
    
    def get_video(self, id):
        """ GET API_PATH/[VIDEO_ID] """
        return defaultMethodResponse

    def put_video(self, id, params):
        """ PUT API_PATH/[VIDEO_ID] """
        return defaultMethodResponse

    def delete_video(self, id):
        """ DELETE API_PATH/[VIDEO_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_video_comments(self, id):
        """ GET API_PATH/[VIDEO_ID]/comments """
        return defaultMethodResponse

    def post_video_comments(self, id, params):
        """ POST API_PATH/[VIDEO_ID]/comments """
        return defaultMethodResponse

    def get_video_likes(self, id, params):
        """ GET API_PATH/[VIDEO_ID]/likes """
        return defaultMethodResponse

    def post_video_likes(self, id, params):
        """ POST API_PATH/[VIDEO_ID]/likes """
        return defaultMethodResponse

    def delete_video_likes(self, id, params):
        """ DELETE API_PATH/[VIDEO_ID]/likes """
        return defaultMethodResponse

    def get_video_dislikes(self, id):
        """ GET API_PATH/[VIDEO_ID]/dislikes """
        return defaultMethodResponse

    def post_video_dislikes(self, id, params):
        """ POST API_PATH/[VIDEO_ID]/dislikes """
        return defaultMethodResponse

    def delete_video_dislikes(self, id):
        """ DELETE API_PATH/[VIDEO_ID]/dislikes """
        return defaultMethodResponse


    #   endregion Connections

    #   endregion Photo Object
    
    
    #   region Folder Aggregation 
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Folder%20Mapping
    
    def format_folder_response(self, params):
        response = {
                        "file": format_file(params),
                        "data": params['data']
                   }
        response.update(format_generic(params))
        return response

    def post_folders(self, params):
        """ POST API_PATH/[ACCOUNT_ID] """
        return defaultMethodResponse

    def get_folder(self, id):
        """ GET API_PATH/[FOLDER_ID] """
        return defaultMethodResponse

    def put_folder(self, id, params):
        """ PUT API_PATH/[FOLDER_ID] """
        return defaultMethodResponse

    def delete_folder(self, id):
        """ DELETE API_PATH/[FOLDER_ID] """
        return defaultMethodResponse

    #   endregion Folder Aggregation

    #   region Album Aggregation
    
    def get_album_audios(self, id, params):
        """ GET API_PATH/[ACCOUNT_ID]/audios """
        return defaultMethodResponse
        
    def post_album_audios(self, id, params):
        """ POST API_PATH/[ALBUM_ID]/audios """
        return defaultMethodResponse

    def get_album_files(self, id):
        """ GET API_PATH/[ACCOUNT_ID]/files """
        return defaultMethodResponse
        
    def post_album_files(self, id, params):
        """ POST API_PATH/[ALBUM_ID]/files """
        return defaultMethodResponse

    def get_album_photos(self, id):
        """ GET API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse
        
    def post_album_photos(self, id, params):
        """ POST API_PATH/[ALBUM_ID]/photos """
        return defaultMethodResponse

    #   endregion Album Aggregation

    #   endregion Media API