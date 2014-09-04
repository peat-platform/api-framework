__author__ = 'mpetyx'

from OPENiapp.OPENiapp.models import Cloudlet
from OPENiapp.cloudletClient import client

from django.conf import settings

def cloudlet_creation_for_user(user):
    """
    post user creation it creates a cloudlet and connects it to a user
    @return:
    """

    response = client.CloudletClient(server=settings.CLOUDLET_SERVER).create(alias=user.id,
                                                                                              username=user.username)

    location = response['body']['id']

    user_cloudlet = Cloudlet(user=user, locationIP=location)
    user_cloudlet.save()

    return True

