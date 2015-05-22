__author__ = 'mpetyx'

import json

import requests


class CloudletClient:
    def __init__(self):

        self.__typesMapping = {
            "Account": "t_774cc4bd416ed4f56feda461005fbba3-893",
            "Address": "t_6a03ca9ab321ef9863218d0f141dfa7b-819",
            "Application": "t_5fe2cc6ce3d41bf89681dfb82e5edbbb-501",
            "Article": "t_4f89584a3b28c3a375405b40bd0276e8-735",
            "Audio": "t_f6c242993d1d8f7c690411fdc41e68a2-733",
            "Badge": "t_fc20846048e073d737ce8b9737cf02ec-525",
            "Base File": "t_b5a8d294f4f8294b8b4e16209f745d63-598",
            "Base Place": "t_723fc77fb49f6de85d176824b1b7a1ec-501",
            "Base Product": "t_a6ce2c7c789321cf81f8127d44822ff8-609",
            "Base Service": "t_9c1573d00777d01ac805bab3ea808af7-609",
            "Base Tags": "t_2ef106dfa4aff6da6690e84f36406773-500",
            "Card": "t_c2178433fb21c298b1e01032703e4259-836",
            "Cart": "t_08fe40271d5936433734c9aed6dd5f33-190",
            "Checkin": "t_8371bfab8e2b26f3aad1684f4ffc623d-439",
            "Comment": "t_24bff7829a6db7af8967a54eaf3ddeb4-523",
            "Context": "t_9d59c558aad360ff5164f40ec3d41ef1-19921",
            "Delivery": "t_51bd2f37bbe344adb297fdbc328ec188-310",
            "Dislike": "t_56955a39281a92f337e0e7060d0c7076-309",
            "Duration": "t_424593cff2a653e8d7a38cf849330c22-284",
            "Event": "t_745b966dfbfdb0f9df08eee9eb235a44-817",
            "Favorite": "t_fd6228f5904ed2f7d6c5efe83b8033c9-310",
            "File": "t_0f40dec4ad67efe24102e5579ff01c3d-725",
            "Folder": "t_9126548342a6f7fbaee0857a3852a8fd-444",
            "Friendship": "t_3a7565af166f5404029ebcc359e04161-312",
            "From": "t_336883fad53f5b87446163781ea5c992-262",
            "Game": "t_5df0eee2c002ef6184f314d766e53d19-624",
            "Group": "t_b4bbaba64f77021b8aead3f12ef50e01-297",
            "Invoice": "t_3c7bdc1aed1373155d7f1ff5e17ec8f1-643",
            "Like": "t_79a86c27354d5c9b53c0d5f6893fa09e-306",
            "Location": "t_5b09fb93c087b6d2c27522b614cd6e55-388",
            "Measurement": "t_7ba720a527e62be93914075479260a30-631",
            "Note": "t_55bc0aae5203bf302e6bba919ae24de8-404",
            "Notebook": "t_3b1242a9c5308ccb3e3c233b53f05ec4-562",
            "Nutrition": "t_ad810a06a5e88738f372ea97480cde16-957",
            "Offer": "t_465fc858b67ecadd8a981fcf29819fd3-529",
            "Order": "t_5defd6ffd64c212528237659ba999737-641",
            "Page": "t_645b0e9a28000aae304ed58abc88cf95-296",
            "Payment": "t_ecb559e9b0659e786f423a52e10b8aa6-193",
            "Person": "t_13675dd2edbf0998a38f3521a1804e16-498",
            "Photo": "t_2ae367b464094c6b01d9fcdd7da677d5-840",
            "Place": "t_a028f8664ebaf6e15326a19151df3485-437",
            "Playlist": "t_ac899ef30c9fcb2915febfe6866b0711-300",
            "Product": "t_2a27e5538556dcf86face99a55ae00b3-628",
            "Question": "t_b607d0ba38373031b8c39def44065e70-467",
            "Question Option": "t_e1b90ff2288c1ab4ce8b3ba9befb968e-538",
            "RSVP": "t_7f8f7d782fd8cfa493bd4c016f39ce70-412",
            "Refund": "t_8db1da29fe0155da4d1a27f2fe2ee89c-642",
            "Registeredapplication": "t_65de6e51b08bdaefb0ca3e1ea011bf77-313",
            "Review": "t_ef448d85997eb987f26a3e44982aadf2-737",
            "Route": "t_02cbdef90a3efd21cadeb1828023539f-531",
            "Score": "t_7425f1681c87d9c0fca44095466e02a5-415",
            "Service": "t_08809b9d67d37f062d536d33148eeab4-628",
            "Shipping": "t_9cf199e310d70395ccbe44fd83536e17-597",
            "Shop": "t_32de9fa77969ba5bb91f9c4f33b5653b-534",
            "Size": "t_cf484e7ebcdc406ea59668599aefd7ba-370",
            "Sleep": "t_1f9137c969dda93517f89eb63d58a0bb-883",
            "Social Account": "t_547214915134b3fc9dfbad8941a3bee5-627",
            "Social Token": "t_4b292a50a8d1bd23c094b9144bdb8bea-399",
            "Socialapp": "t_568facb7d8a59a38630075bc854ef603-599",
            "Status": "t_b3b71b7b2ddb834324f54b7c7875c243-406",
            "Tag": "t_6a2dd7c23d45a0283cfe328eef766e72-527",
            "Time": "t_82f0947c63b17b09a40b0aecde5aedf2-408",
            "Travel": "t_87910b71db0b7ece114e7014a8071691-532",
            "User": "t_e9d13c200cb9c4840292fbf71a59d1e6-1353",
            "Video": "t_a8325d11623b400636703a93a325f7db-733",
            "Wallet": "t_2da67ee16717bf45877bd297bb19e046-418",
            "Workout": "t_62e71d0529c810a267c65d989b5c3b15-1163"
        }
        


    def getTypeId(self, typeId):
        return self.__typesMapping[str(typeId)]


    def retrieve_cloudlet_id(self, host, token):

        hdr = {"Authorization": str(token)}
        r = requests.get(url=str(host) + ":443/api/v1/cloudlets", headers=hdr, verify=False)

        try:
            self.__cloudlet_id = r.json()['id']
        except:
            self.__cloudlet_id = 1

        return {"status code": r.status_code, "body": r.text, "json_response": r.json(),
                "cloudlet_id": self.__cloudlet_id}


    def delete(self, host, auth_token, id):

        headers = {"content-type": "application/json", "Authorization": str(auth_token)}

        r = requests.delete(url=str(host) + ":443/api/v1/objects/" + str(id), headers=headers)

        return {"status code": r.status_code, "body": r.text, "json response": r.json()}


    def post_object(self, host, auth_token, object):

        headers = {"content-type": "application/json", "Authorization": str(auth_token)}

        r = requests.post(url=str(host) + ":443/api/v1/objects/", data=json.dumps(object), headers=headers,
                          verify=False)

        return {"status code": r.status_code, "body": r.text}  # , "json response":r.json()}


    def get_object_list(self, host, auth_token):

        headers = {"content-type": "application/json", "Authorization": str(auth_token)}

        r = requests.get(url=str(host) + ":443/api/v1/objects/", headers=headers, verify=False)

        return {"status code": r.status_code, "body": r.text, "json response": r.json()}


    def get_object_by_id(self, host, auth_token, id):

        headers = {"content-type": "application/json", "Authorization": str(auth_token)}

        r = requests.get(url=str(host) + ":443/api/v1/objects/" + str(id), headers=headers, verify=False)

        return {"status code": r.status_code, "body": r.text, "json response": r.json()}


    def get_objects_by_type(self, host, auth_token, type):

        type_id = self.__typesMapping[str(type)]

        endpoint = str(host) + ":443/api/v1" + "/objects/?type=" + str(type_id)
        headers = {"content-type": "application/json", "Authorization": str(auth_token)}

        return requests.get(url=endpoint, verify=False, headers=headers)
