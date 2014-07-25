from unittest import TestCase

__author__ = 'mpetyx'


class TestCloudletClient(TestCase):

    # Setting up the cloudlet the connection
    def setUp(self):

        print "Set up cloudlet connection"

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "Closing the connection to the cloudlet"
        print "finalising the test"

    def test_post_object(self):
        self.fail()

    def test_get_object_if(self):
        self.fail()