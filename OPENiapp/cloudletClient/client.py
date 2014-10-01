__author__ = 'mpetyx'

import json

import requests


class CloudletClient:
    def __init__(self, server, username=None, password=None):
        self.__username = username
        self.__password = password
        self.__server = server
        self.__auth = (self.__username, self.__password)
        self.__cloudlet_id = None
        # self.__auth_headers={"auth_token": '{ "token": { "user": "%"}, "signature": "%s" }'%(self.__username,self.__password )}

    def create(self, alias, username):
        payload = {
            "id": "",
            "alias": alias,
            "username": username,
            "date_created": "",
            "_revision": ""
        }

        r = requests.post(url=self.__server, data=json.dumps(payload))

        return {"status code": r.status_code, "body": r.text, "json response": r.json()}

    def retrieve_cloudlet_id(self):
        # hdr = {
        # "auth_token": '{"token": { "user": "mpetyx" }, "signature": "eyJhbGciOiJSUzI1NiJ9.eyJqdGkiOiJlM2Y1YzFkMi0yYzE0LTRiZDEtYmIyMC05NjBlMmVmYWIxOWIiLCJzdWIiOiIyOWQxMDFjNi01MDIzLTQxMWQtYTkzZS00OWI3MGYxMzgwYmMiLCJzY29wZSI6WyJvcGVuaWQiXSwiY2xpZW50X2lkIjoibXBldHl4IiwiY2lkIjoibXBldHl4IiwidXNlcl9pZCI6IjI5ZDEwMWM2LTUwMjMtNDExZC1hOTNlLTQ5YjcwZjEzODBiYyIsInVzZXJfbmFtZSI6Im1wZXR5eCIsImVtYWlsIjoiZW1haWxAZXhhbXBsZS5vcmciLCJpYXQiOjE0MTIxNTgyOTMsImV4cCI6MTQxMjIwMTQ5MywiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3VhYS9vYXV0aC90b2tlbiIsImF1ZCI6WyJvcGVuaWQiXX0.RNXaukUgIaEO3d1lDZAumOBgdp7c-8vLIzZ465ANE06MXB-caeEXdDGbi7W4Qse8p4iwl8g4A_wWuBbXQ9S-iw""}'}

        hdr = { "Authorization":self.__password}
        r = requests.get(url=self.__server + "/cloudlets", headers=hdr, verify=False)

        print r
        try:
            self.__cloudlet_id = r.json()['id']
        except:
            self.__cloudlet_id = 1

        return {"status code": r.status_code, "body": r.text, "json_response": r.json(),
                "cloudlet_id": self.__cloudlet_id}


    def delete(self, id):
        r = requests.delete(url=self.__server + "/" + str(id))

        return {"status code": r.status_code, "body": r.text, "json response": r.json()}


    def post_object(self, object):

        # sample_object = {
        #     "@openi_type": "t_0e09a80a6411bb7203e1d4e3bd1fc85f-321",
        #     "@data": {
        #     "name" : "clark",
        #     "service" : "krypton",
        #     "email":"clark@kent.com"
        #     }
        # }

        if not self.__cloudlet_id:
            self.retrieve_cloudlet_id()

        r = requests.post(url=self.__server + "/objects/" + str(self.__cloudlet_id), data=json.dumps(object), verify=False)

        return {"status code": r.status_code, "body": r.text}#, "json response":r.json()}

    def get_object_if(self):
        r = requests.get(url=self.__server + "/objects/{cloudletId}/{objectId}", auth=self.__auth)

        return {"status code": r.status_code, "body": r.text, "json response": r.json()}

    def get_object_list(self):
        if not self.__cloudlet_id:
            self.retrieve_cloudlet_id()
        r = requests.get(url=self.__server + "/objects/" + str(self.__cloudlet_id), verify=False)

        return {"status code": r.status_code, "body": r.text, "json response": r.json()}

    def get_object_by_id(self, id):
        if not self.__cloudlet_id:
            self.retrieve_cloudlet_id()
        r = requests.get(url=self.__server + "/objects/" + str(self.__cloudlet_id) + "/" + str(id), verify=False)

        return {"status code": r.status_code, "body": r.text, "json response": r.json()}

if __name__ == '__main__':


    client = CloudletClient("https://demo2.openi-ict.eu:443/api/v1", "mpetyx","eyJhbGciOiJSUzI1NiJ9.eyJqdGkiOiJlM2Y1YzFkMi0yYzE0LTRiZDEtYmIyMC05NjBlMmVmYWIxOWIiLCJzdWIiOiIyOWQxMDFjNi01MDIzLTQxMWQtYTkzZS00OWI3MGYxMzgwYmMiLCJzY29wZSI6WyJvcGVuaWQiXSwiY2xpZW50X2lkIjoibXBldHl4IiwiY2lkIjoibXBldHl4IiwidXNlcl9pZCI6IjI5ZDEwMWM2LTUwMjMtNDExZC1hOTNlLTQ5YjcwZjEzODBiYyIsInVzZXJfbmFtZSI6Im1wZXR5eCIsImVtYWlsIjoiZW1haWxAZXhhbXBsZS5vcmciLCJpYXQiOjE0MTIxNTgyOTMsImV4cCI6MTQxMjIwMTQ5MywiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3VhYS9vYXV0aC90b2tlbiIsImF1ZCI6WyJvcGVuaWQiXX0.RNXaukUgIaEO3d1lDZAumOBgdp7c-8vLIzZ465ANE06MXB-caeEXdDGbi7W4Qse8p4iwl8g4A_wWuBbXQ9S-iw")
    # print client.create(alias="jor el", username="kent")['body']
    # client.delete("c_0669d9dec1d9b80db1f0455746c25a0e")
    print client.retrieve_cloudlet_id()
    print client.get_object_list()

    sample_object = {
        "@openi_type": "t_0e09a80a6411bb7203e1d4e3bd1fc85f-321",
        "@data": {
            "name": "michael",
            "service": "vril",
            "email": "michael@mpetyx.com"
        }
    }

    print client.post_object(sample_object)

    # sample_object_id = "o_d7c856d6f7fc743212c924a1e7d7e84a-126"
    #
    # print client.get_object_by_id(sample_object_id)