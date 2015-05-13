__author__ = 'mpetyx'

import json

import requests


class CloudletClient:
    def __init__(self):

        self.__typesMapping = {

           "Account": "t_b93f2a4deba48a3af4d227585fc2ed5f-865",
           "Address": "t_5d64c0d9aec202b3640d6299a77c1509-791",
           "Application": "t_e6d1ad84f27aadaa2cde753eb3d4b317-485",
           "Article": "t_b376d655ccb9a33f84457a34604a380e-715",
           "Audio": "t_bfdd68f275b1906db96f75243b2f773e-713",
           "Badge": "t_89c4271f51061d130b6d43fbb42740d1-509",
           "BaseFile": "t_e279a7e2d27b6179586f22bdd7b5e570-578",
           "BasePlace": "t_589117a5960861422d0c4e91a785128d-485",
           "BaseProduct": "t_81f0c6b3d531ff6da134853083d77699-589",
           "BaseService": "t_660e99b91a4516ea9818d2d5b5150358-589",
           "BaseTags": "t_5ca072c38980aaa0ddd0de0e543dde2e-484",
           "Card": "t_ef3c706c576730bf65735685095db63d-812",
           "Cart": "t_09a17ade3b2e27b6425a1e5ff6248a59-186",
           "Checkin": "t_522ac89ccff14b4ca4e72c0af489b92f-427",
           "Comment": "t_b624b6ef0457d61dc0a2419f75fb0799-507",
           "Context": "t_120d7910fbf7c10e2cf87a66fb144976-19397",
           "Delivery": "t_ff8b3f3e04459f7038d476e53fd313ac-302",
           "Dislike": "t_bc2626641a77487b67546a0f22291af0-301",
           "Duration": "t_1040fe0c6738d54e3a62d80f4c1c49e7-276",
           "Event": "t_60d502360a18fb97423171806e862e75-793",
           "Favorite": "t_c20e1d149f53c6cd3f356c7b5a8280d0-302",
           "File": "t_8ee7f53195482660a42437cfe880e54b-705",
           "Folder": "t_80c8d22dd804ef68186e7e366efc3a8e-432",
           "Friendship": "t_85a89798f460934bcdac3574e6ea0861-304",
           "From": "t_e5732e3f05643e6c484c9ae13be48001-254",
           "Game": "t_d9eca744df83900f86204987c949fe91-604",
           "Group": "t_dac214724d76969469fadaa550fd4d5f-289",
           "Invoice": "t_e18d3e14d14d882d89f9e956c22f4346-623",
           "Like": "t_410ab91b3f86fc4fda2842c9ee0d55b2-298",
           "Location": "t_8cd98b0bc66ec5bd1867af6b37a9c01e-376",
           "Measurement": "t_bd47b3275378fe86e595c90efaf8e2c8-611",
           "Note": "t_f967677746b819e758489231358ea34d-392",
           "Notebook": "t_fab62cc062f315eed9c85b063acaba0d-546",
           "Nutrition": "t_7eb626f059c43bf536b1e6391d34d59d-925",
           "Offer": "t_7e1eec04d4540d821603c339ff570cb0-513",
           "Order": "t_51c69bffad6929fc6b9b48a5370370af-621",
           "Page": "t_15b3b4383e2a4c649fd823d37b05acd3-288",
           "Payment": "t_518bf73e494604df36b9a059bac3079f-189",
           "Person": "t_7d440d30ceccddd3a1e1ac04425b09f0-482",
           "Photo": "t_6af039bf23da26c7156b57c535b93396-816",
           "Place": "t_499326432c9ae9d79607c4b9890d8f27-425",
           "Playlist": "t_1dcc5866aea31601fb455e80b0b8b394-292",
           "Product": "t_6f7b1dfa891d6c528234f572f9446a87-608",
           "Question": "t_c4d24047874198b37eee38e7c04089ab-455",
           "Question Option": "t_6f35831238bb34d4d4689335dd40cb72-522",
           "RSVP": "t_3ad6c9c16f2ff41bf5e976a35a07c88c-400",
           "Refund": "t_36648b9941f31e8f4c3356476905511c-622",
           "Registered Application": "t_7230be77ebdea76f7131dfb39b135d41-305",
           "Review": "t_85572c9aff2ea47726772e13c577e620-713",
           "Route": "t_014e970bd921076002b0473fba324324-515",
           "Score": "t_3b829d76212756f8c0b3f34521a7043a-403",
           "Service": "t_e605d039cbcc792816380ec9befa7128-608",
           "Shop": "t_d2d1c6575ec239314e4f5f59be17da13-518",
           "Size": "t_581bd788bd6d112413b9f33b1b7e246b-358",
           "Sleep": "t_4c00d1636357e277385ec1924fd75e07-855",
           "SocialAccount": "t_af70ff4d1a91c1cea7cdbacf627a4736-607",
           "SocialToken": "t_286c07b8387c0d453c41e53d39706178-387",
           "Socialapp": "t_c9f5a81f5ba999f24b61a952d3a3143e-579",
           "Status": "t_1e7a8342b31933784201c7be1275152d-394",
           "Tag": "t_62058bae827be452ce97ad537924ab5a-511",
           "Time": "t_efc40aac249938660d2c0fd024f368ae-396",
           "Travel": "t_bb4abe1d1dc06601108a8298fbd5ed3b-516",
           "User": "t_d91f2355ae455825062a4ae26106beca-1309",
           "Video": "t_b8d3c700575632964d3f44f83c1f9ed3-713",
           "Wallet": "t_925c432568e3ecbf541a09fb69facbd0-406",
           "Workout": "t_27baf6080473cef861a4ac9b9e0a3507-1127"
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
