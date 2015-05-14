__author__ = 'mpetyx'

import requests
import json

class Permissions:

    def __init__(self, request):

        self.__typesMapping = {
            "Duration": "t_57aa803ed7073091b029311179470fa2-511",
            "From": "t_e7da1ccaf11067a0cfbcc3135b0bb893-710",
            "Location": "t_03accb81d4175ccfbd07d85a25fd4f59-615",
            "Time": "t_e5185def1d44d7739e76d48ae37065fa-635",
            "Context": "t_6a8dcdb4929dfc485220e07a4746f517-20049",
            "BaseFile": "t_ad7cf4249f504c19bbd91947e456313e-825",
            "BaseTags": "t_4cd750ec0f4f8fc3dce38ba9f5cc60cb-727",
            "Person": "t_5719179a223b5887490b19e30e234b05-725",
            "Address": "t_0ef6b52e84d5f321a31109a4f945b80c-1046",
            "Place": "t_33e80cc634e3958155eade0418444163-1004",
            "QuestionOption": "t_1c27cdb5fe5d57d0be65ac693c817e08-1137",
            "Note": "t_5eb8a34d8af2f94387fe7762161d2d11-1003",
            "Tag": "t_fde81112b0f07f4990e4acfa6586ff43-1126",
            "BaseTags": "t_27e9945d2f8eb3191f7627817afaf7c3-511",
            "Audio": "t_356d522e9636d39d8b4271de19b3e3fc-744",
            "Account": "t_003b070598d1e6ea42ee012f69797f3e-904",
            "BasePlace": "t_5446a44426c6eb3406b93dc4324f0283-512",
            "Badge": "t_e4666b60c93428ae2ac4e86f182093bc-536",
            "BaseFile": "t_a6cf0b308a05eb4221603e4ae948a932-609",
            "BaseService": "t_9b27ef4e159de850efc13a0ad7be34cc-620",
            "BaseProduct": "t_d3076c6b2964ce65c677408e7b03db7d-620",
            "Card": "t_defd14d3070bb4978880f7731a547f35-847",
            "Duration": "t_e59660359432ef8f9fbbe9a9545997f1-295",
            "Delivery": "t_1a2e99928b46258f5595bc8d69163835-321",
            "Event": "t_e2209ffb250ca8a3fd3f703ec7a39b1c-829",
            "Cart": "t_9b77fe2bcd6c287abbc9e7f5ee61e19e-201",
            "Checkin": "t_74bad307ed27072dbc67357a536182bd-451",
            "Game": "t_7a45b237651ffd95f0f32113a975d15b-635",
            "Comment": "t_dd4e84c5782c11cf33d78139cbc033c6-534",
            "Group": "t_04ab7e23e50aef2c8a9ff84080288d2c-308",
            "Like": "t_14022c94deaf9b4823ce9ef7467e2ea5-317",
            "Folder": "t_eae587900c6e187a3755f6bea22b6935-455",
            "Friendship": "t_729e42d0e58c751ecd551690ec50fb1a-323",
            "File": "t_2e1b6aed698e4630fcc1107220b8abd0-736",
            "Dislike": "t_99163fdce55f96dc3c5b578fd66e32a8-320",
            "Favorite": "t_81dc7a23af580ca8b92ef27d9d6596d5-321",
            "Place": "t_c035b1961f382ead508f9017776fb5e0-449",
            "Review": "t_d78f9af47df1aa5c3a11d05f5525cafe-748",
            "Notebook": "t_bd068748c43d0fdfc0024299317b8805-574",
            "Playlist": "t_158df926d43c72a4aab7ab526ca70c97-311",
            "Photo": "t_f57e85d10963ba6a099aebce8ab6dc37-818",
            "Nutrition": "t_99de92a9d44caea2d97b26e6ed35227f-968",
            "Page": "t_9d759545d4f3f1d676cc553ff8043e6e-307",
            "Person": "t_ecb7f1b65a183f2370816ad70174daf2-509",
            "Product": "t_60808aa730d2b159ac2aac09608440c5-639",
            "QuestionOption": "t_eaf168e43e463c0f8e9c2b658e9c4145-549",
            "Question": "t_478df8057cd294ec28976302f48392f2-478",
            "Refund": "t_358083137ae44158960796f9c79f3637-653",
            "RSVP": "t_0c847413571ecb6fc086de1633a53c8c-423",
            "Registeredapplication": "t_657cb076d656dff2f437a178ffa1c9f1-324",
            "Service": "t_8d6a9ab10e64818663f7f9c572bc3cbd-639",
            "SocialToken": "t_9337b6ed7ed5e55a99a8aa38bcb431fc-410",
            "Route": "t_f8d4838e27a2b358dca40638c713b001-542",
            "Size": "t_8d0ff9a1e66eb16af7d6bd071b0b62d5-381",
            "Sleep": "t_36a567283fd624e3c83d3bc7c00115d7-894",
            "Payment": "t_b7718914115f5adc8620e77a484d8e6d-204",
            "Offer": "t_dc1982be238d812825370d1f2ea74e80-540",
            "Order": "t_01c6e9585fd4693152646d697644cfb8-652",
            "Measurement": "t_05b33abdc75a04ffaf2f494ecf79c5da-642",
            "Note": "t_1d54a3b9897e2abd311d1cba6287aed7-415",
            "From": "t_ac6ad2ce039d200ded6668a1df35c7b6-273",
            "Location": "t_0578381d8207a9302a6b31b9510bb098-399",
            "Invoice": "t_5e1bc6397f3d48e10cef5e972ccfb038-654",
            "Score": "t_7e035b17875b7ce038e062a676282347-426",
            "Shipping": "t_2b6aefecc27259707c8615a7952f5fc5-608",
            "Shop": "t_b3acf8c93a59241b363169c68d0fc6ba-545",
            "Socialapp": "t_cc373c0f1180a40227e85966ce38c64e-610",
            "Status": "t_0aea698a28b44d4bf84203a384ad959b-417",
            "Tag": "t_341aead8a032f444e2b0dc5b188686a8-538",
            "Time": "t_72876c1e8d7e5db900218ae740400377-419",
            "Workout": "t_4dc2ad82b0f66bba949216b5fbaa3aff-1174",
            "Travel": "t_bddcb376b8cb4ec620bc4ef2ad179f2a-543",
            "Video": "t_b59e0e11991dd54b5487d06d9f9000e7-744",
            "User": "t_af0c2cd1c2917e4f3433025e35f3d3cd-1364",
            "Wallet": "t_c78fe73adb747f7810a5e6bc18344f17-429",
            "Application": "t_7888a698d1fe10a8f05e67279f6d6897-512",
            "Article": "t_89b960476249cf9b4f25ad1cf66c394a-746",
            "Address": "t_173c11907da9df7352baad31d10a683e-830",
            "SocialAccount": "t_4492825f8bc18e080aed5ff3160fb6d7-638"
        }

        auth_token = request.META['HTTP_AUTHORIZATION']

        headers = {"content-type": "application/json", "Authorization": str(auth_token)}
        self.body = requests.get(url="https://demo2.openi-ict.eu/api/v1/permissions/", verify=False, headers=headers).json()

    def getTypeId(self, typeId):
        return self.__typesMapping[str(typeId)]

    def print_permissions(self):

        for perm in self.body:
            print perm

    def permissions_verified(self, method, object_type):

        if method=='get':
            method = 'READ'
        elif method=='post':
            method = 'CREATE'
        elif method=='put':
            method = 'UPDATE'
        elif method=='delete':
            method = 'DELETE'

        for perm in self.body:
            if perm['access_type']==method and self.getTypeId(object_type.title())==perm['ref']:
                return 1


        return 0