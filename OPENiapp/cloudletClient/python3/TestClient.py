__author__ = 'mpetyx'

from ObjectsApi import ObjectsApi
from swagger import ApiClient



if __name__ == '__main__':


    # client = CloudletClient("https://193.1.188.34:443/api/v1", "dmccarthy",
    #                         "cVnf/YsH/h+554tlAAh5CvyLr3Y9xrqAK4zxTA/C8PMDWcjcUZistg90H2HiCL/tAL3VZe/53VbJcrFZGyFZDw==")
    # print client.create(alias="jor el", username="kent")['body']
    # client.delete("c_0669d9dec1d9b80db1f0455746c25a0e")
    # print client.retrieve_cloudlet_id()
    # print client.get_object_list()

    sample_object = {
        "@type": "t_0e09a80a6411bb7203e1d4e3bd1fc85f-321",
        "@data": {
            "name": "michael",
            "service": "vril",
            "email": "michael@mpetyx.com"
        }
    }

    apiKey = {
        "auth_token": '{"token": { "user": "dmccarthy" }, "signature": "cVnf/YsH/h+554tlAAh5CvyLr3Y9xrqAK4zxTA/C8PMDWcjcUZistg90H2HiCL/tAL3VZe/53VbJcrFZGyFZDw=="}'}

    clientAPI = ApiClient(apiKey=apiKey,apiServer="https://193.1.188.34:443/api/v1")
    client = ObjectsApi(apiClient=clientAPI)
    client.createObject(cloudletId="c_a136c28ce7e970c27c5a36593c2990df-60", body=sample_object)
