__author__ = 'mpetyx'

import json

import requests


class CloudletClient:
    def __init__(self, server, username, password):
        self.__username = username
        self.__password = password
        self.__server = server
        self.__auth = (self.__username, self.__password)

    def create(self, alias, username):
        payload = {
            "id": "",
            "alias": alias,
            "username": username,
            "date_created": "",
            "_revision": ""
        }

        r = requests.post(url=self.__server, data=json.dumps(payload))

        return {"status code": r.status_code, "body": r.text, "json response":r.json()}

    def details(self, id):
        r = requests.get(url=self.__server+"/"+str(id))

        return {"status code": r.status_code, "body": r.text, "json response":r.json()}


    def delete(self, id):
        r = requests.delete(url=self.__server + "/" + str(id))

        return {"status code": r.status_code, "body": r.text, "json response":r.json()}


    def post_object(self, object):
        payload = {'object': object, 'user': self.__username}

        r = requests.post(url=self.__server, auth=self.__auth, data=json.dumps(payload))

        return {"status code": r.status_code}#, "body":r.text}#, "json response":r.json()}

    def get_object_if(self):
        r = requests.get(url=self.__server + "/objects/{cloudletId}/{objectId}", auth=self.__auth)

        return {"status code": r.status_code, "body": r.text, "json response":r.json()}


client = CloudletClient("http://193.1.188.34:80/api/v1/cloudlets", "mpetyx", "yo")
# print client.create(alias="jor el", username="kent")
# client.delete("c_0669d9dec1d9b80db1f0455746c25a0e")
# print client.details("c_16c21af80178b0ee20b874b515d16cba")