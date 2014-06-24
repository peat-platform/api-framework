from common import *

class bcMedia:
    #   region Media API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Media%20API/
    
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
    
    def get_a_photo(self, params):
        """ GET API_PATH/[PHOTO_ID] """
        return defaultMethodResponse

    def get_all_photos_for_account(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse

    def post_photo_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse

    def get_all_photos_for_album(self, params):
        """ GET API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse
        
    def post_photo_to_album(self, params):
        """ POST API_PATH/[ALBUM_ID]/photos """
        return defaultMethodResponse

    def share_a_photo(self, params):
        """ Share a photo (not available for OPENi - only Tumblr) """
        return defaultMethodResponse

    def edit_a_photo(self, params):
        """ PUT API_PATH/[PHOTO_ID] """
        return defaultMethodResponse

    def delete_a_photo(self, params):
        """ DELETE API_PATH/[PHOTO_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_comments_for_photo(self, params):
        """ GET API_PATH/[PHOTO_ID]/comments """
        return defaultMethodResponse

    def post_comment_to_photo(self, params):
        """ POST API_PATH/[PHOTO_ID]/comments """
        return defaultMethodResponse

    def delete_comment_from_photo(self, params):
        """ DELETE API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def edit_comment_of_photo(self, params):
        """ PUT API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def like_photo(self, params):
        """ POST API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def get_likes_for_photo(self, params):
        """ GET API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def unlike_photo(self, params):
        """ DELETE API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def dislike_photo(self, params):
        """ POST API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse

    def get_dislikes_for_photo(self, params):
        """ GET API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse

    def delete_dislikes_of__photo(self, params):
        """ DELETE API_PATH/[PHOTO_ID]/dislikes """
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

    def get_a_folder(self, params):
        """ GET API_PATH/[FOLDER_ID] """
        return defaultMethodResponse

    def post_folder_to_account(self, params):
        """ POST API_PATH/[ACCOUNT_ID] """
        return defaultMethodResponse

    def edit_a_folder(self, params):
        """ PUT API_PATH/[FOLDER_ID] """
        return defaultMethodResponse

    def delete_a_folder(self, params):
        """ DELETE API_PATH/[FOLDER_ID] """
        return defaultMethodResponse

    #   endregion Folder Aggregation

    #   endregion Media API