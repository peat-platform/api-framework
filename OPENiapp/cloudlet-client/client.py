__author__ = 'mpetyx'

import requests
import json

class CloudletClient:

    def __init__(self, server, username,password):

        self.__username = username
        self.__password = password
        self.__server = server
        self.__auth = (self.__username, self.__password)


    def post_object(self, object):

        payload = {'object':object, 'user':self.__username}

        r = requests.post(url=self.__server, auth=self.__auth, data=json.dumps(payload) )

        return {"status code":r.status_code}#, "body":r.text}#, "json response":r.json()}

    def get_object_if(self):
        r = requests.get(url=self.__server+"/objects/{cloudletId}/{objectId}", auth=self.__auth)

        return {"status code":r.status_code, "body":r.text}#, "json response":r.json()}

client = CloudletClient("http://www.facebook.com","mpetyx","yo")
print client.post_object("yo")