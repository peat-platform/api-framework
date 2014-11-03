from OPENiapp.Providers.base.media import bcMedia
from OPENiapp.Providers.base.common import *
import os
from apiclient.http import MediaFileUpload

class ytMedia(bcMedia):
    """ This class is used to: 
        VIDEO MAPPING
        1.  Get a Youtube video
        2.  Get all Youtube videos for an account
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

    def get_video(self, id):
        """ GET API_PATH/[VIDEO_ID] """
        metadata = self.connector.videos().list(id = id, part = "id, snippet, recordingDetails, fileDetails").execute()
        raw_data = metadata['items'][0]
        
        names = ['id', 'object_type', 'service', 'resource_uri', 'from_id', 'from_object_type', 'from_resource_uri', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon'])
        names.extend(['location_latitude', 'location_longitude', 'location_height'])
        names.extend(['duration_starts_time', 'duration_ends_time'])
        names.extend(['tags'])

        fields = ['id', 'object_type', 'service', '', '', '', '', '', 'recordingDetails.recordingDate', '', '']
        fields.extend(['snippet.title', 'snippet.description', 'fileDetails.fileType', 'fileDetails.fileSize', 'thumbnails.default.url'])
        fields.extend(['recordingDetails.location.latitude', 'recordingDetails.location.longitude', 'recordingDetails.location.altitude'])
        fields.extend(['', 'contentDetails.duration'])
        fields.extend(['snippet.tags'])

        alternatives = ['', 'video', 'youtube', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', '', '', ''])
        alternatives.extend(['', '', ''])
        alternatives.extend(['', ''])
        alternatives.extend([''])

        data = self.get_fields(raw_data, names, fields, alternatives)
        
        response = {
                    'meta':
                        {
                         'total_count': 1,
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'objects': [self.format_video_response(data)]
                    }

        # Curate tag array from Youtube
        #Only text-tags in youtube, no location, no time
        tag_array = []
        if (check_if_exists(raw_data, 'snippet.tags') != defJsonRes):
            for tag in metadata.get("items", []):
                    tag_names = ['tags_id', 'tags_name', 'tags_time_created_time', 'tags_time_edited_time', 'tags_time_deleted_time', 'tags_x-location', 'tags_y-location']
                    tag_fields = ['', 'snippet.tags' , '', '', '', '', '']
                    tag_alternatives = ['', '', '', '', '', '', '']
                    tag_data = self.get_fields(tag, tag_names, tag_fields, tag_alternatives)
                    tag_array.append(format_tags(tag_data))
        response['objects'][0]['tags'] = tag_array
        
        return response

    def get_videos(self):
        return self.get_all_videos_for_account('me')

    def get_all_videos_for_account(self, id):
        """ GET API_PATH/[ACCOUNT_ID]/videos """
        channels_response = self.connector.channels().list(
          mine=True,
          part="contentDetails"
        ).execute()
        
        for channel in channels_response["items"]:
          uploads_list_id = channel["contentDetails"]["relatedPlaylists"]["uploads"]
          
        playlistitems_list_request = self.connector.playlistItems().list(
            playlistId=uploads_list_id,
            part="snippet",
            maxResults=50
        )
    
        playlistitems_list_response = playlistitems_list_request.execute()
        
        i=0
        
        names = ['id', 'object_type', 'service', 'resource_uri', 'from_id', 'from_object_type', 'from_resource_uri', 'from_name', 'time_created_time', 'time_edited_time', 'time_deleted_time']
        names.extend(['file_title', 'file_description', 'file_format', 'file_size', 'file_icon'])
        names.extend(['location_latitude', 'location_longitude', 'location_height'])
        names.extend(['duration_starts_time', 'duration_ends_time'])
        names.extend(['tags'])

        fields = ['id', 'object_type', 'service', '', '', '', '', '', 'recordingDetails.recordingDate', '', '']
        fields.extend(['snippet.title', 'snippet.description', 'fileDetails.fileType', 'fileDetails.fileSize', 'thumbnails.default.url'])
        fields.extend(['recordingDetails.location.latitude', 'recordingDetails.location.longitude', 'recordingDetails.location.altitude'])
        fields.extend(['', 'contentDetails.duration'])
        fields.extend(['snippet.tags'])

        alternatives = ['', 'video', 'youtube', '', '', '', '', '', '', '', '']
        alternatives.extend(['', '', '', '', ''])
        alternatives.extend(['', '', ''])
        alternatives.extend(['', ''])
        alternatives.extend([''])
        
        response = {
                    'meta':
                        {
                         'total_count': [],
                         'previous': defJsonRes,
                         'next': defJsonRes
                        },
                    'objects': []
                    }
    
        for playlist_item in playlistitems_list_response["items"]:
            metadata = self.connector.videos().list(id =playlist_item["snippet"]["resourceId"]["videoId"], part = "id, snippet, recordingDetails, fileDetails").execute()
            raw_datas = metadata['items'][0]
  
            for raw_data in metadata.get("items", []):
                data = self.get_fields(raw_datas, names, fields, alternatives)
                response['objects'].append(self.format_video_response(data))
                i +=1
                print response

            tag_array = []
            if (check_if_exists(raw_datas, 'snippet.tags') != defJsonRes):
                for tag in metadata.get("items", []):
                        tag_names = ['tags_id', 'tags_name', 'tags_time_created_time', 'tags_time_edited_time', 'tags_time_deleted_time', 'tags_x-location', 'tags_y-location']
                        tag_fields = ['', 'snippet.tags' , '', '', '', '', '']
                        tag_alternatives = ['', '', '', '', '', '', '']
                        tag_data = self.get_fields(tag, tag_names, tag_fields, tag_alternatives)
                        tag_array.append(format_tags(tag_data))
                response['objects'][0]['tags'] = tag_array  
                
            response['meta']['total_count'] = i   

        return response
          

    def post_videos(self, params):
        """ POST API_PATH/[ACCOUNT_ID]/videos """
        if (check_if_exists(params, 'source') != defJsonRes):
            tags = None
            if params['keywords']:
                tags = params['keywords'].split(",")
            
            body=dict(
                snippet=dict(
                  title= params['title'],
                  description= params['description'],
                  tags=tags
                ),
                status=dict(
                  privacyStatus= params['privacyStatus']
                )
              )
            
            # Call the API's videos.insert method to create and upload the video.
            return self.connector.videos().insert(
                part=",".join(body.keys()),
                body=body,
                media_body=MediaFileUpload(params['source'], chunksize=-1, resumable=True)
              ).execute()
            
        return "Insufficient Parameters"
            
    def post_video_to_aggregation(self, params):
        """ POST API_PATH/[AGGREGATION_ID]/videos """        
        #youtube playlist -> aggregation
        if (check_if_exists(params, 'source') != defJsonRes):
            tags = None
            if params['keywords']:
                tags = params['keywords'].split(",")
             
            body=dict(
                snippet=dict(
                  title= params['title'],
                  description= params['description'],
                  tags=tags
                ),
                status=dict(
                  privacyStatus= params['privacyStatus']
                )
              )
             
            # Call the API's videos.insert method to create and upload the video.
            uploaded_video = self.connector.videos().insert(
                part=",".join(body.keys()),
                body=body,
                media_body=MediaFileUpload(params['source'], chunksize=-1, resumable=True)
              ).execute()
             
            return self.connector.playlistItems().insert(part="snippet", body={'snippet': {'playlistId': params['playlistID'],'resourceId': {'kind': 'youtube#video','videoId': uploaded_video['id']}}}
            ).execute()
        return "Insufficient Parameters"

    def delete_video(self, id):
        """ DELETE API_PATH/[VIDEO_ID] """
        return self.connector.videos().delete(id=id).execute()
    
    #   region Connections

    def get_video_comments(self, id):
        """ GET API_PATH/[VIDEO_ID]/comments """
        #not longer in youtube api v3
        return defaultMethodResponse

    def post_video_comments(self, id):
        """ POST API_PATH/[VIDEO_ID]/comments """
         #not longer in youtube api v3
        return defaultMethodResponse

    def post_video_likes(self, id):
        """ POST API_PATH/[VIDEO_ID]/likes """
        return self.connector.videos().rate(id=id, rating="like").execute()

    # To-Do: Does this return anything?
    def get_video_likes(self, id):
        """ GET API_PATH/[VIDEO_ID]/likes """
        metadata = self.connector.videos().list(id = id, part = "statistics").execute()
        raw_datas = metadata['items'][0]
        print raw_datas

        response = {
                    'meta':
                        {
                            'total_count': raw_datas['statistics']['likeCount'],
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'objects': []
                    }
        
        return response

    def delete_video_likes(self, id):
        """ DELETE API_PATH/[VIDEO_ID]/likes """
        return self.connector.videos().rate(id = id, rating="none").execute()

    def post_video_dislikes(self, id):
        """ POST API_PATH/[VIDEO_ID]/dislikes """
        return self.connector.videos().rate(id = id, rating="dislike").execute()
    
    # To-Do: Does this return anything?
    def get_video_dislikes(self, id):
        """ GET API_PATH/[VIDEO_ID]/dislikes """
        metadata = self.connector.videos().list(id = id, part = "statistics").execute()
        raw_datas = metadata['items'][0]
        print raw_datas

        response = {
                    'meta':
                        {
                            'total_count': raw_datas['statistics']['dislikeCount'],
                            'previous': self.check_if_exists(raw_datas, 'paging.previous'),
                            'next': self.check_if_exists(raw_datas, 'paging.next')
                        },
                    'objects': []
                    }
        
        return response

    #   endregion Connections

    #   endregion Video Object