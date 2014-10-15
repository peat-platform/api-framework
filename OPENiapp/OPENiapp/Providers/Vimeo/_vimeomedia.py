from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *
import os

class vimeoMedia(bcMedia):
    """ This class is used to:       
        VIDEO MAPPING
        1. Get a Vimeo video
        2. Get all Vimeo videos for an account
        3. Post a video to a simple account
        4. Get a video for an account
        5. Edit a video 
        6. Delete a video   
        
    """
    #   region Media API

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

    #   endregion Video Object
    
    #   endregion Media API
