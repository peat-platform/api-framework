__author__ = 'mpetyx'

import json

import requests


class CloudletClient:
    def __init__(self):

        self.__typesMapping = {"Audio":"t_eb3b2abb860e2028da3794e5161d62d4-743",
                                "Badge":"t_e782776271a49e49d1e1dc3f32ee59b1-535",
                                "BaseFile":"t_a6cf0b308a05eb4221603e4ae948a932-609",
                                "BasePlace":"t_5446a44426c6eb3406b93dc4324f0283-512",
                                "Article":"t_19a1ed1eccf2d5e3cacea912d98f91b5-745",
                                "BaseProduct":"t_d3076c6b2964ce65c677408e7b03db7d-620",
                                "BaseService":"t_9b27ef4e159de850efc13a0ad7be34cc-620",
                                "BaseTags":"t_27e9945d2f8eb3191f7627817afaf7c3-511",
                                "Cart":"t_e38aaf95bf5c3141266944aa8d0db42c-200",
                                "Card":"t_c8ac686ccb6f1bb125570b43c86d92be-846",
                                "Comment":"t_44d99b0045707b0e1ecc2ff5d1d589c9-533",
                                "Checkin":"t_d84a06d6b1c601a16d493ab0fd10ceec-450",
                                "Delivery":"t_b01e6b08e35b163186fb9026aa0e308d-320",
                                "Dislike":"t_6b0a095814cf2ed720928bea771adaf8-319",
                                "Duration":"t_e59660359432ef8f9fbbe9a9545997f1-295",
                                "Event":"t_805f6af2031bde2a14e909cdc25aad3d-828",
                                "Favorite":"t_a6999c7d55c7571d27e310909d63f7b1-320",
                                "File":"t_0c91d4437d02eadb995725b673f380b2-735",
                                "Folder":"t_faa3573413f54f220e6e46a1ba018f73-454",
                                "Friendship":"t_c9bcc78f2e3b861e7571dbf64d50027f-322",
                                "From":"t_ac6ad2ce039d200ded6668a1df35c7b6-273",
                                "Game":"t_1908d6881e5d65d7090f4a53cef4a323-634",
                                "Group":"t_3123b463894526532b56af0534286bd0-307",
                                "Invoice":"t_e4480b359aeeb11c3a0c4b95ad3ef8cc-653",
                                "Like":"t_339bd1a3bc179c04da399919be1e14ee-316",
                                "Measurement":"t_8954a822010d9fb2a344fbab35328e44-641",
                                "Location":"t_0578381d8207a9302a6b31b9510bb098-399",
                                "Notebook":"t_8b194bddeadc6f151224ccf937bfb739-573",
                                "Note":"t_e856f08a88d70284580352afff82ec12-414",
                                "Offer":"t_a9e9da3b860f13971472e9f02ec0b1c7-539",
                                "Nutrition":"t_cf66ce4d4cdf08636b78742cc005332a-967",
                                "Page":"t_f6ad0c5eaa0484f08e0bf719b9f21d4b-306",
                                "Order":"t_09cef7bb9200857b146a3f99258c699f-651",
                                "Payment":"t_fae8e91a11158e542d0ebe7540666191-203",
                                "Person":"t_ecb7f1b65a183f2370816ad70174daf2-509",
                                "Photo":"t_682c8f8b85cece5e8fabe4e35999cf83-855",
                                "Place":"t_f821b856efcadf03516374863c829b44-448",
                                "Playlist":"t_9cbda173497438adc39bf32d3d13360a-310",
                                "Product":"t_40122ca32ad4d9f2ec28241835264fa6-638",
                                "Question":"t_537fbe1bbbe65cade121a31f8adef58e-477",
                                "QuestionOption":"t_d98051f52cbf083d8cc9dc15e91f34d2-548",
                                "RSVP":"t_384e3e678eb9a43d3e17d68d2bb745ff-422",
                                "Refund":"t_ecb7c2e1d3044a617ca5bd75324ccb11-652",
                                "Registeredapplication":"t_f12a4ae6944f678d55337417515942b6-323",
                                "Review":"t_7c03345881248e2d590edb9ad7f126b1-747",
                                "Route":"t_aa0471b8f4f598f923d167b11d451b4b-541",
                                "Score":"t_22ca16accd6a5883a9df2e463b5916e1-425",
                                "Service":"t_613359e6e063e2e4ae27083cce39d4ea-638",
                                "Shop":"t_67867678e86ff7ffd078b33103a88987-544",
                                "Shipping":"t_70fc9aae2be5ad5d7269d608dd2e784c-607",
                                "Size":"t_8d0ff9a1e66eb16af7d6bd071b0b62d5-381",
                                "Sleep":"t_c1bf8cb333751dd71add0ad746f08757-893",
                                "SocialAccount":"t_4492825f8bc18e080aed5ff3160fb6d7-638",
                                "SocialToken":"t_9337b6ed7ed5e55a99a8aa38bcb431fc-410",
                                "Status":"t_d1425bc98c4fb206b9f063bd9f979fda-416",
                                "Socialapp":"t_cc373c0f1180a40227e85966ce38c64e-610",
                                "Time":"t_72876c1e8d7e5db900218ae740400377-419",
                                "Tag":"t_b0ea3adfdf97471093b71730baaabe24-537",
                                "Travel":"t_9b64b070d09037d224568a13d2111148-542",
                                "User":"t_402d94dd3b59ecd8cce7e037f32932cb-1363",
                                "Video":"t_bd3ea322c9b29d0280b4b915098ecb69-743",
                                "Wallet":"t_cc9178ba0c9167197f8c897e31bc9949-428",
                                "Workout":"t_873cce8ce90ee7e2af5480c0c8304c41-1173",
                                "Application":"t_7888a698d1fe10a8f05e67279f6d6897-512",
                                "Account":"t_461bd372452568d4c620c2572ebebe5d-903",
                                "Address":"t_173c11907da9df7352baad31d10a683e-830"}
       


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

        return {"status code": r.status_code, "body": r.text}#, "json response":r.json()}


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
