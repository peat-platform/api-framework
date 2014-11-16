__author__ = 'mpetyx'

import json

import requests


class CloudletClient:

    def __init__(self):
        self.__typesMapping = {"Badge":"t_09160db089761755705c865fc9d5e024-644","Card":"t_f4f47e629a82b03ca743ec3110df2923-1003","Cart":"t_cef196cc21c9c788e308c253685ae80f-227","Checkin":"t_b8a6b61f08434f3b1eee25d02d3547f6-538","Comment":"t_bbcc65f545bd3fb6bb0e2ef2d680fa10-650","Audio":"t_4fcb843ee85b823d68efb86ff460076e-362","Delivery":"t_a059625ba0f3d323a537458a9ad0b7d3-381","Dislike":"t_58bab863e5fd1991d6ddc5af5758d837-378","Duration":"t_bc147a198ad30afd701bddbd67af58ea-355","Favorite":"t_4f5d1d3bbba1b026f58da72fa4c2cd66-381","Event":"t_4440bd77c20363dff11de120b37fb829-991","File":"t_06694347713618245de72929de5aef0f-359","Folder":"t_f3f33ce3500612959d3529e58d1b097f-365","From":"t_b5fa50f7c5321f3cc86b787bde495157-325","Friendship":"t_24f0dda726be2aa3f53ae420231f18ea-387","Group":"t_4e69411d98fc421f9a1e414fe87cef26-362","Game":"t_b972174208744357e9e0804c6435a5f5-765","Invoice":"t_dfc2d05e746adedce574f8abea32b9ef-799","Like":"t_f2263576ba10d7d5ba4e505394482ad9-369","Measurement":"t_5b3ca8c1463a7d17b11fd69181a1e886-807","Location":"t_83916b9dee063a1b37675fd9b9943870-489","Note":"t_fdf106cfb3e2658e838422ac6d5dde63-493","Notebook":"t_e3ffd8d9faa9af341f7159e99a78d876-523","Nutrition":"t_b3137ecfcd2503802876a6892cc1281e-1216","Offer":"t_192e1b5ce4aa919d3ef304ae62227669-648","Page":"t_e14a62745c1c03255c6d071e4f60567a-359","Order":"t_e96967dda8617b1831947ee1767dae73-787","Payment":"t_d309c9de0bfa3fc2de9ff966a90691cc-233","PersonModel":"t_e8fc11781b83cba447fde91a4592bc6b-646","Photo":"t_cfd6002df6517180ec479ee9c80a093c-640","Place":"t_23dabdd642497b312de48a5c7a36b4e2-362","Product":"t_030022c5b33c4159ccaeeba1861a00f0-784","Playlist":"t_590cdf21f02da349021fe3aee4d0161c-371","Question":"t_504417b2e7057b9eea1ae765b3c62efe-568","QuestionOption":"t_a26cf2e6745eb3b8b9f246c58137de2b-693","RSVP":"t_adeefcfc47933b11cacedd36e0a8e902-501","Refund":"t_e575ce98c3c2dfb2071f6db1fbbf8eeb-793","Registeredapplication":"t_c34968f38304225485550efc9991a14f-410","Review":"t_cbc82392fd050eb5e654cc64a5b1537e-916","Route":"t_8b2e1afd2d21c0c7c860396b11e7a511-650","Score":"t_fb0541d01ddd1606db71a38b75582770-507","Service":"t_18e84a08e84237ae9a6c3fb43926ec4a-784","Shipping":"t_0eb31350f3ad38636ea8a47c669e1ff9-377","Shop":"t_8978a214e1d5e3fda7402ddd6036c47d-649","Sleep":"t_f73ae1947b2a515213684bce1c46a011-1083","SocialAccount":"t_70d949d8bcdb410aacf4c453b87c6b14-813","SocialToken":"t_afb91d829b80e98a1c7c911d49459cc0-509","Socialapp":"t_30dc4551bf8afefa339e351a1e8a9302-765","Status":"t_11668154ecf71d64e4ae948d59d44b77-501","Tag":"t_2c02c7265a8ba090f4370898df36aab8-638","Time":"t_3488e85e9780e9f4eb1cad9da5c4c1be-497","Travel":"t_358d379f130b10a21b3981606f725d47-655","User":"t_04ce46c08270f979662e61955c2ec22f-1650","Video":"t_394e16bd3ef40a6e114a1ea8bd2a2f57-362","Wallet":"t_fd647de3a0299b8aa11963a970857091-513","Workout":"t_99e07ee31abdf463a531009c2fce6a28-1435","Article":"t_1d695dff41ec39a4506d98e6ce3d4ce9-511","Account":"t_3b7acd26ecdd0f2e19cd941742a0ea72-1107","Application":"t_45de298b3749ffcd7ba721af63494ab0-241","Place":"t_07f915e19bf1fcb2ffc2753b7de9d930-1331","QuestionOption":"t_7eb64b97aa79ec65985d12f3f5e4ba24-1715","Context":"t_62972a935f36a48aa910142a419d68db-10776","Duration":"t_cbf71123ba750a0042dc766349dcb613-611","From":"t_82cbf3dea2ce17a87c6c39b052664f1e-836","Location":"t_30abfa7d0dd88a9ec300ae79a36ea4b5-740","Person":"t_8213235e114e431d56cc78e41fe3d794-898","Time":"t_649b7359f952c5fc440e9ae6817aad8f-740"}


    def getTypeId(self, typeId):
        return self.__typesMapping[str(typeId)]


    def retrieve_cloudlet_id(self, host, token):

        hdr = { "Authorization":str(token)}
        r = requests.get(url=str(host)+":443/api/v1/cloudlets", headers=hdr, verify=False)

        try:
            self.__cloudlet_id = r.json()['id']
        except:
            self.__cloudlet_id = 1

        return {"status code": r.status_code, "body": r.text, "json_response": r.json(),
                "cloudlet_id": self.__cloudlet_id}


    def delete(self, host, auth_token, id):

        headers  ={"content-type":"application/json", "Authorization":str(auth_token)}

        r = requests.delete(url=str(host)+":443/api/v1/objects/"+str(id), headers=headers)

        return {"status code": r.status_code, "body": r.text, "json response": r.json()}


    def post_object(self, host, auth_token, object):

        headers = {"content-type":"application/json", "Authorization":str(auth_token)}

        r = requests.post(url=str(host)+":443/api/v1/objects/", data=json.dumps(object), headers=headers, verify=False)

        return {"status code": r.status_code, "body": r.text}#, "json response":r.json()}


    def get_object_list(self, host, auth_token):

        headers = {"content-type":"application/json", "Authorization":str(auth_token)}

        r = requests.get(url=str(host)+":443/api/v1/objects/", headers=headers, verify=False)

        return {"status code": r.status_code, "body": r.text, "json response": r.json()}


    def get_object_by_id(self, host, auth_token, id):

        headers = {"content-type":"application/json", "Authorization":str(auth_token)}

        r = requests.get(url=str(host)+":443/api/v1/objects/" + str(id), headers=headers, verify=False)

        return {"status code": r.status_code, "body": r.text, "json response": r.json()}


    def get_objects_by_type(self, host, auth_token, type):

        type_id = self.__typesMapping[str(type)]

        endpoint = str(host)+":443/api/v1" + "/objects/?type=" + str(type_id)
        headers  = {"content-type":"application/json", "Authorization":str(auth_token)}

        return requests.get(url=endpoint, verify=False, headers=headers)
