from common import *

class bcMedia:
    #   region Media API
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Media%20API/
    
    #   region Photo Object
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/photo/

    def format_photo_response(self, data):
        response = {
                        "file": format_file(data),
                        "location": format_location(data),
                        "tags": data['tags'],
                        "height": data['height'],
                        "width": data['width']
                   }
        response.update(format_generic(data))
        return response
    
    def get_a_photo(self, data):
        """ GET API_PATH/[PHOTO_ID] """
        return defaultMethodResponse

    def get_all_photos_for_account(self, data):
        """ GET API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse

    def post_photo_to_account(self, data):
        """ POST API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse

    def get_all_photos_for_album(self, data):
        """ GET API_PATH/[ACCOUNT_ID]/photos """
        return defaultMethodResponse
        
    def post_photo_to_album(self, data):
        """ POST API_PATH/[ALBUM_ID]/photos """
        return defaultMethodResponse

    def share_a_photo(self, data):
        """ Share a photo (not available for OPENi - only Tumblr) """
        return defaultMethodResponse

    def edit_a_photo(self, data):
        """ PUT API_PATH/[PHOTO_ID] """
        return defaultMethodResponse

    def delete_a_photo(self, data):
        """ DELETE API_PATH/[PHOTO_ID] """
        return defaultMethodResponse
    
    #   region Connections

    def get_photo_comments(self, data):
        """ GET API_PATH/[PHOTO_ID]/comments """
        return defaultMethodResponse

    def post_photo_comment(self, data):
        """ POST API_PATH/[PHOTO_ID]/comments """
        return defaultMethodResponse

    def delete_photo_comment(self, data):
        """ DELETE API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def edit_photo_comment(self, data):
        """ PUT API_PATH/[COMMENT_ID] """
        return defaultMethodResponse

    def like_a_photo(self, data):
        """ POST API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def get_photo_likes(self, data):
        """ GET API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def unlike_photo(self, data):
        """ DELETE API_PATH/[PHOTO_ID]/likes """
        return defaultMethodResponse

    def dislike_photo(self, data):
        """ POST API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse

    def get_photo_dislikes(self, data):
        """ GET API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse

    def delete_photo_dislikes(self, data):
        """ DELETE API_PATH/[PHOTO_ID]/dislikes """
        return defaultMethodResponse


    #   endregion Connections

    #   endregion Photo Object
    
    
    #   region Folder Aggregation 
    #   As described here: https://opensourceprojects.eu/p/openi/wiki/Folder%20Mapping
    
    def format_folder_response(self, data):
        response = {
                        "file": format_file(data),
                        "data": data['data']
                   }
        response.update(format_generic(data))
        return response

    def get_a_folder(self, data):
        """ GET API_PATH/[FOLDER_ID] """
        return defaultMethodResponse

    def post_folder_to_account(self, data):
        """ POST API_PATH/[ACCOUNT_ID] """
        return defaultMethodResponse

    def edit_a_folder(self, data):
        """ PUT API_PATH/[FOLDER_ID] """
        return defaultMethodResponse

    def delete_a_folder(self, data):
        """ DELETE API_PATH/[FOLDER_ID] """
        return defaultMethodResponse

    #   endregion Folder Aggregation

    #   endregion Media API