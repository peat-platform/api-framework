from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *
import os

class odMedia(bcMedia):
    """ This class is used to:
        AUDIO MAPPING
        1.  Get a Onedrive audio
        2.  Get all Onedrive audios for an account
        3.  Post a audio to a simple account
        4.  Get all audios from an Onedrive album
        5.  Post a audio to an Onedrive album
        6.  Edit a audio 
        7.  Delete a audio
        
        FILE MAPPING
        8.  Get a Onedrive file
        9.  Get all Onedrive files for an account
        10.  Post a file to a simple account
        11.  Get all files from an Onedrive album
        12.  Post a file to an Onedrive album
        13.  Edit a file 
        14.  Delete a file
    
        PHOTO MAPPING
        15.  Get a Onedrive photo
        16.  Get all Onedrive photos for an account
        17. Post a photo to a simple account
        18. Get all photos from an Onedrive album
        19. Post a photo to an Onedrive album
        20. Edit a photo 
        21. Delete a photo
        
        VIDEO MAPPING
        22. Get a Onedrive video
        23. Get all Onedrive videos for an account
        24. Post a video to a simple account
        25. Get a video for an account
        26. Edit a video 
        27. Delete a video  
        
        FOLDER MAPPING
        28. Get a Onedrive folder
        29. Post a folder
        30. Delete a folder  
        
    """
    #   region Media API

    #   region Audio Object  
    def get_audio(self, id):
        """ GET API_PATH/[AUDIO_ID] """
        return defaultMethodResponse

    def get_account_audios(self, id):
        """ GET API_PATH/[ACCOUNT_ID]/audios """
        return defaultMethodResponse

    def post_audio(self, id, params):
        """ POST API_PATH/[ACCOUNT_ID]/audio """
        return defaultMethodResponse

    def get_album_audios(self, id, params):
        """ GET API_PATH/[ACCOUNT_ID]/audios """
        return defaultMethodResponse
        
    def post_album_audio(self, id, params):
        """ POST API_PATH/[ALBUM_ID]/audios """
        return defaultMethodResponse

    def edit_audio(self, id, params):
        """ PUT API_PATH/[AUDIO_ID] """
        return defaultMethodResponse

    def delete_audio(self, id):
        """ DELETE API_PATH/[AUDIO_ID] """
        return defaultMethodResponse
    
    #   region Connections

    #   endregion AUDIO Object


    #   region File Object
    
    def get_file(self, id):
        """ GET API_PATH/[FILE_ID] """
        return defaultMethodResponse

    def get_account_files(self, id):
        """ GET API_PATH/[ACCOUNT_ID]/files """
        return defaultMethodResponse

    def post_file(self, id, params):
        """ POST API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse

    def get_album_files(self, id):
        """ GET API_PATH/[ACCOUNT_ID]/files """
        return defaultMethodResponse
        
    def post_album_file(self, id, params):
        """ POST API_PATH/[ALBUM_ID]/files """
        return defaultMethodResponse

    def edit_file(self, id, params):
        """ PUT API_PATH/[FILE_ID] """
        return defaultMethodResponse

    def delete_file(self, id):
        """ DELETE API_PATH/[FILE_ID] """
        return defaultMethodResponse
    
    #   region Connections

    #   endregion File Object

    
    #   region Photo Object
    
    def get_photo(self, id):
        """ GET API_PATH/[PHOTO_ID] """
        return defaultMethodResponse

    def get_account_photos(self, id):
        """ GET API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse

    def post_photo(self, id, params):
        """ POST API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse

    def get_album_photos(self, id):
        """ GET API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse
        
    def post_album_photo(self, id, params):
        """ POST API_PATH/[ALBUM_ID]/photos """
        return defaultMethodResponse

    def edit_photo(self, id, params):
        """ PUT API_PATH/[PHOTO_ID] """
        return defaultMethodResponse

    def delete_photo(self, id):
        """ DELETE API_PATH/[PHOTO_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_photo_comments(self, id):
        """ GET API_PATH/[PHOTO_ID]/comments """
        return defaultMethodResponse

    def post_photo_comment(self, id, params):
        """ POST API_PATH/[PHOTO_ID]/comments """
        return defaultMethodResponse

    def delete_photo_comment(self, id):
        """ DELETE API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def edit_photo_comment(self, id, params):
        """ PUT API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def post_photo_like(self, id, params):
        """ POST API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def get_photo_likes(self, id):
        """ GET API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def post_photo_unlike(self, id, params):
        """ DELETE API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def post_photo_dislike(self, id, params):
        """ POST API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse

    def get_photo_dislikes(self, id):
        """ GET API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse

    def delete_photo_dislikes(self, id):
        """ DELETE API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse


    #   endregion Connections

    #   endregion Photo Object
    
    #   region Video Object
    
    def get_video(self, id):
        """ GET API_PATH/[VIDEO_ID] """
        return defaultMethodResponse

    def get_account_videos(self, id):
        """ GET API_PATH/[ACCOUNT_ID]/videos """
        return defaultMethodResponse

    def post_account_video(self, id, params):
        """ POST API_PATH/[ACCOUNT_ID]/videos """
        return defaultMethodResponse
        
    def post_aggregation_video(self, id, params):
        """ POST API_PATH/[AGGREGATION_ID]/videos """
        return defaultMethodResponse

    def edit_video(self, id, params):
        """ PUT API_PATH/[VIDEO_ID] """
        return defaultMethodResponse

    def delete_video(self, id):
        """ DELETE API_PATH/[VIDEO_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_video_comments(self, id):
        """ GET API_PATH/[VIDEO_ID]/comments """
        return defaultMethodResponse

    def post_video_comment(self, id, params):
        """ POST API_PATH/[VIDEO_ID]/comments """
        return defaultMethodResponse

    def post_video_like(self, id, params):
        """ POST API_PATH/[VIDEO_ID]/likes """
        return defaultMethodResponse

    def get_video_likes(self, id, params):
        """ GET API_PATH/[VIDEO_ID]/likes """
        return defaultMethodResponse

    def post_video_unlike(self, id, params):
        """ DELETE API_PATH/[VIDEO_ID]/likes """
        return defaultMethodResponse

    def post_video_dislike(self, id, params):
        """ POST API_PATH/[VIDEO_ID]/dislikes """
        return defaultMethodResponse

    def get_video_dislikes(self, id):
        """ GET API_PATH/[VIDEO_ID]/dislikes """
        return defaultMethodResponse

    def delete_video_dislikes(self, id):
        """ DELETE API_PATH/[VIDEO_ID]/dislikes """
        return defaultMethodResponse


    #   endregion Connections

    #   endregion Photo Object
    
    
    #   region Folder Aggregation 

    def get_folder(self, id):
        """ GET API_PATH/[FOLDER_ID] """
        return defaultMethodResponse

    def post_account_folder(self, id, params):
        """ POST API_PATH/[ACCOUNT_ID] """
        return defaultMethodResponse

    def edit_folder(self, id, params):
        """ PUT API_PATH/[FOLDER_ID] """
        return defaultMethodResponse

    def delete_folder(self, id):
        """ DELETE API_PATH/[FOLDER_ID] """
        return defaultMethodResponse

    #   endregion Folder Aggregation

    #   endregion Media API
