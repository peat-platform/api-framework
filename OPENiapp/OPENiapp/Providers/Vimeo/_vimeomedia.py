from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *
import os

class vimeoMedia(bcMedia):
    """ This class is used to: 
        VIDEO MAPPING
        1.  Get a Vimeo video
        2.  Get all Vimeo videos for an account
        3.  Post a video to a simple account
        4.  Post a video to aggregation
        5.  Edit a video 
        6.  Delete a video 
        
        7.  Get comments for video
        8.  Post comment to video
        9.  Like video
        10. Get Likes for video
        11. Unlike video 
        12. Get dislikes for video
        13. Delete dislikes for video
        
    """
    #   region Media API
    
    #   region Video Object

    def get_a_video(self, data):
        """ GET API_PATH/[VIDEO_ID] """
        return defaultMethodResponse

    def get_all_videos_for_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/videos """
        return defaultMethodResponse

    def post_video_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/videos """
        return defaultMethodResponse
        
    def post_video_to_aggregation(self, params):
        """ POST API_PATH/[AGGREGATION_ID]/videos """
        return defaultMethodResponse

    def edit_a_video(self, params):
        """ PUT API_PATH/[VIDEO_ID] """
        return defaultMethodResponse

    def delete_a_video(self, params):
        """ DELETE API_PATH/[VIDEO_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_comments_for_video(self, params):
        """ GET API_PATH/[VIDEO_ID]/comments """
        return defaultMethodResponse

    def post_comment_to_video(self, params):
        """ POST API_PATH/[VIDEO_ID]/comments """
        return defaultMethodResponse

    def like_video(self, params):
        """ POST API_PATH/[VIDEO_ID]/likes """
        return defaultMethodResponse

    def get_likes_for_video(self, params):
        """ GET API_PATH/[VIDEO_ID]/likes """
        return defaultMethodResponse

    def unlike_video(self, params):
        """ DELETE API_PATH/[VIDEO_ID]/likes """
        return defaultMethodResponse

    def dislike_video(self, params):
        """ POST API_PATH/[VIDEO_ID]/dislikes """
        return defaultMethodResponse

    def get_dislikes_for_video(self, params):
        """ GET API_PATH/[VIDEO_ID]/dislikes """
        return defaultMethodResponse

    def delete_dislikes_of_video(self, params):
        """ DELETE API_PATH/[VIDEO_ID]/dislikes """
        return defaultMethodResponse

    #   endregion Connections

    #   endregion Video Object