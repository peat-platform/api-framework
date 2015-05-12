from unittest import TestCase
import unittest
import logging
import sys
import string
import random

from client import CloudletClient
__author__ = 'mpetyx'


class TestCloudletClient(TestCase):

    """
    1. Create cloudlet
    2. Get cloudlet by id
    3. Create an object
    4. Retrieve the object by id
    5. Retrieve the object list
    6. Delete the object
    7. Delete the cloudlet
    """
    # Setting up the cloudlet the connection
    def setUp(self):

        self.log= logging.getLogger( "SomeTest.testSomething" )
        self.log.debug( "Set up cloudlet connection")
        self.client = CloudletClient("https://193.1.188.34:443/api/v1", "dmccarthy",
                        "cVnf/YsH/h+554tlAAh5CvyLr3Y9xrqAK4zxTA/C8PMDWcjcUZistg90H2HiCL/tAL3VZe/53VbJcrFZGyFZDw==")



    def test_get_id(self):

        self.log.debug( "About to retrieve the cloudlet it")
        self.assertEquals("c_a136c28ce7e970c27c5a36593c2990df-60", self.client.retrieve_cloudlet_id()['cloudlet_id'])

    def test_retrieve_object_list(self):
        response = self.client.get_object_list()
        self.assertIsNotNone(response)

    def test_get_object_by_id(self):
        sample_object_id = "o_d7c856d6f7fc743212c924a1e7d7e84a-126"
        expected_body = {'body': u'{"@id":"o_d7c856d6f7fc743212c924a1e7d7e84a-126","@location":"https://193.1.188.34/api/v1/objects/c_a136c28ce7e970c27c5a36593c2990df-60/o_d7c856d6f7fc743212c924a1e7d7e84a-126","@cloudlet":"c_a136c28ce7e970c27c5a36593c2990df-60","@type":"https://193.1.188.34/api/v1/types/t_0e09a80a6411bb7203e1d4e3bd1fc85f-321","@data":{"name":"clark","service":"krypton","email":"clark@kent.com"},"_date_created":"2014-09-11T09:36:56.725Z","_date_modified":"2014-09-11T09:36:56.725Z","_revision":"1361641984-1174933891"}', 'status code': 200, 'json response': {u'_date_modified': u'2014-09-11T09:36:56.725Z', u'_revision': u'1361641984-1174933891', u'@cloudlet': u'c_a136c28ce7e970c27c5a36593c2990df-60', u'@location': u'https://193.1.188.34/api/v1/objects/c_a136c28ce7e970c27c5a36593c2990df-60/o_d7c856d6f7fc743212c924a1e7d7e84a-126', u'_date_created': u'2014-09-11T09:36:56.725Z', u'@id': u'o_d7c856d6f7fc743212c924a1e7d7e84a-126', u'@data': {u'name': u'clark', u'service': u'krypton', u'email': u'clark@kent.com'}, u'@type': u'https://193.1.188.34/api/v1/types/t_0e09a80a6411bb7203e1d4e3bd1fc85f-321'}}
        response = self.client.get_object_by_id(sample_object_id)
        self.assertEqual(response,expected_body)

    def test_post_new_object(self):
        chars=string.ascii_uppercase + string.digits
        size = 6
        name = ''.join(random.choice(chars) for _ in range(size))
        sample_object = {
        "@type": "t_0e09a80a6411bb7203e1d4e3bd1fc85f-321",
        "@data": {
            "name": name,
            "service": "vril2",
            "email": "michael2@mpetyx.com"
        }
        }

        self.assertEqual(self.client.post_object(sample_object)['status code'],201)


    # def test_post_object(self):
    #     self.fail()
    #
    # def test_get_object_if(self):
    #     self.fail()

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        self.log.debug( "Closing the connection to the cloudlet")
        self.log.debug( "finalising the test")

if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "SomeTest.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()