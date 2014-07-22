__author__ = 'mpetyx'

import logging

from OPENiapp.models import Person

def profileJson(person):

    response = {}

    if type(person) == int:
        person = Person.objects.get(id=person)



    response["id"] = person.id
    response["name"] = person.user.first_name
    response["surname"] = person.user.last_name
    response["username"] = person.user.username

    try:
        response["profile_pic"] = person.photo.photo_original.url
    except:
        response["profile_pic"] = None
    response["is_available"] = False # Needs to be changed

    return response