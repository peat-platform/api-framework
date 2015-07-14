__author__ = 'mpetyx'

import requests


class Permissions:
    def __init__(self, request):

        self.__typesMapping = {
            "Account": "t_0b26774118f2346c002dd2aa26e04b7a-893",
            "Address": "t_761844902f476e8692ac08fd58d8fa84-965",
            "Application": "t_67340b757ad7bd333b39371d50c19143-759",
            "Article": "t_fea8e7552fadeaab142ff063d7b5f0a2-735",
            "Audio": "t_b66cfc57bf8b01eb21de1b1abe578f5d-733",
            "Badge": "t_eac9b1c9e3a05b1d735825cec0706367-525",
            "BaseFile": "t_d768619c494e7205f8e5cce388dc14d0-744",
            "BasePlace": "t_7509588a1f33ff91c9b16f9b67e4d48b-647",
            "BaseProduct": "t_bc0a6d40af9e95756bda48f467ce421b-755",
            "BaseService": "t_bdaa4bb533a03222b9c4a046ae94f268-755",
            "BaseTag": "t_80351af68d4131695d529f83f9dbdb36-645",
            "Card": "t_9ffc86b54c67e2829924dba5854ae1b1-836",
            "Cart": "t_705cf5dd774aa494d8cc064df4bce0ae-190",
            "Checkin": "t_9685fe7bba5715a7ca9c09995c94e27f-439",
            "Comment": "t_7ab758f7a55cc6f4e1d12a8090da3972-523",
            "Context": "t_1b9325069fd28e2a173716e760f8fb11-19921",
            "Delivery": "t_487513505627ffa6d1cc6cb595950508-310",
            "Dislike": "t_5f557d41e2c903e6182c0af1e9f3c3fa-309",
            "Duration": "t_b70ea7e839aac9575fa13d94abaf53aa-430",
            "Event": "t_9e22473c4ca1a2eae3520b14b946ae4a-817",
            "Favorite": "t_7764b5ff0a2e8ff45cf5ae3d6f336a21-310",
            "File": "t_a92a93d61b87501c823d180f4159191a-724",
            "Folder": "t_3b862e5f3377de644e8c80a578658ae6-444",
            "Friendship": "t_bf53930538509787ddb6266b057930b5-312",
            "From": "t_4ab89466467a24f9a693580d019f8b31-408",
            "Game": "t_8ba8b6827c6fb21f511667a8fe4272f9-624",
            "Group": "t_faa5fc94d5cba53feddc5e14a7dc1c51-297",
            "Invoice": "t_17e87978301c8cae369971f46e054190-640",
            "Like": "t_7ae2a3515d3ab487cc9802c9b626922e-306",
            "Location": "t_fee26aabe253d6705b6743860fc758d7-534",
            "Measurement": "t_64cbc67bfab54e114e3349007af9c82f-631",
            "Note": "t_83eefc5b546e7d7158f2af37850246f5-404",
            "Notebook": "t_223ba8fb60fb6ffd4932781b8673f011-560",
            "Nutrition": "t_750c8f077eb3922491818a1f2e0b8e62-957",
            "Offer": "t_4bd6833ca84193de23c627cc969e3041-529",
            "Order": "t_23f7517bf9cc56f560cf41079b27b1e8-638",
            "Organization": "t_5741bcf00c3f57b99e8b391ec57cca78-648",
            "Page": "t_e3342e550f17a1e3b5c2239e96939fde-296",
            "Payment": "t_6a044722ba9bc28abdfd1ba8de8ae7f5-193",
            "Person": "t_9bf5aa346a8e3c0dbaa388fad7ea19f0-644",
            "Photo": "t_13d9404ad831f2ad50f6a255b0db185d-837",
            "Place": "t_b717b01ca8c3b3664bc980d05a5cb0b1-445",
            "Playlist": "t_225bcd9db8fab272ca0ce0755ccb4ece-300",
            "Product": "t_e77b6738b5f2a4e9cddb8e0cf422972d-627",
            "Question": "t_b95cf308ac8ce51751db91f709700cbe-466",
            "QuestionOption": "t_6f37bb651473dc72dafb191dea40e868-538",
            "RSVP": "t_06aa1f6c3657f0c89fc6971c68a236b6-412",
            "Refund": "t_8c644cb41ee62c64a3a8f18751c03034-641",
            "Registeredapplication": "t_78eb424c97dbd06d4dbacd0c6fbdfefb-313",
            "Review": "t_bf4c5a6ed2113c20409b1ad43791f3e3-736",
            "Route": "t_d3120d358c2d5ee291c3d928339c777c-531",
            "Score": "t_c28bae3f1490f1cc42a7847aa0354b1a-414",
            "Service": "t_2e5ad7877ef615a8134b2bbceb57788c-627",
            "Shipping": "t_e0485ca451628f03134ff23877804358-597",
            "Shop": "t_ec61ce3f77226b1eb3b5de44c99dfe9b-534",
            "Size": "t_172452d943cac44201403266d44d0824-516",
            "Sleep": "t_a89740e1a1162708eb0e428e2a5cea80-883",
            "SocialAccount": "t_59e15ff427956eee4958656d34cec55e-627",
            "SocialToken": "t_07d4b5e82387901e10b2c40cce330cc8-399",
            "Socialapp": "t_8b62b4c4549db0c5402ec4ea064ed89a-599",
            "Status": "t_cdf936bcba55d479c5f025f733471666-406",
            "Tag": "t_f4d81a4bf072acc1574a2d026773f2ec-527",
            "Time": "t_620c1d7608d470586b1cc152c6f56afb-554",
            "Travel": "t_6d9a1a8ea563a681a37248c8aa16640e-532",
            "User": "t_248266d3180e50e17d58e27516fe6337-1353",
            "Video": "t_a057afd1e60c918cfb2f06808a954848-733",
            "Wallet": "t_a08f59796619bbc9c33da81571f38659-418",
            "Workout": "t_8fa48856cc5f355b18349eaa5195c26e-1163"
        }

        auth_token = request.META['HTTP_AUTHORIZATION']

        headers = {"content-type": "application/json", "Authorization": str(auth_token)}
        self.body = requests.get(url="https://demo2.openi-ict.eu/api/v1/permissions/", verify=False,
                                 headers=headers).json()

    def getTypeId(self, typeId):
        return self.__typesMapping[str(typeId)]

    def print_permissions(self):

        for perm in self.body:
            print "permission:", perm
            # print perm

    def permissions_verified(self, method, object_type):

        if method == 'get':
            method = 'READ'
        elif method == 'post':
            method = 'CREATE'
        elif method == 'put':
            method = 'UPDATE'
        elif method == 'delete':
            method = 'DELETE'

        try:
            for perm in self.body:
                if 'access_type' in perm.keys():
                    if perm['access_type'] == method and self.getTypeId(object_type.title()) == perm['ref']:
                        return 1
        except:
            pass

        return 0
