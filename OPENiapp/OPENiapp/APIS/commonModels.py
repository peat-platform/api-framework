from OPENiapp.OPENiapp.APIS.Context.models import OpeniContextAwareModel

from OPENiapp.OPENiapp.APIS.Profile.Account.models import OpeniAccount

from django.db import models

#   Set of Properties
class AddressModel():
    street = models.TextField()
    number = models.TextField()
    apartment = models.TextField()
    city = models.TextField()
    locality = models.TextField()
    country = models.TextField()
    zip = models.TextField()

class DurationModel():
    starts_time = models.TextField()
    ends_time = models.TextField()

class FromModel():
    from_id = models.TextField()
    object_type = models.TextField()
    url = models.TextField()
    name = models.TextField()

class LocationModel():
    latitude = models.TextField()
    longitude = models.TextField()
    height = models.TextField()

class SizeModel():
    depth = models.TextField()
    height = models.TextField()
    width = models.TextField()

class TagsModel():
    tag_id = models.TextField()
    name = models.TextField()
    Time = models.ForeignKey(TimeModel)
    x_location = models.TextField()
    y_location = models.TextField()

class TimeModel():
    created_time = models.TextField()
    edited_time = models.TextField()
    deleted_time = models.TextField()

#   Profile

class ApplicationModel():
    title = models.TextField()
    description = models.TextField()
    version = models.TextField()
    icon = models.TextField()
    developer = models.TextField()

class DeviceModel():
    manufacturer = models.TextField()
    model = models.TextField()
    device_id = models.TextField()
    os_type = models.TextField()
    os_version = models.TextField()

class FileModel():
    title = models.TextField()
    description = models.TextField()
    format = models.TextField()
    size = models.TextField()
    icon = models.TextField()

class OrganizationModel():
    name = models.TextField()
    description = models.TextField()
    founded = models.TextField()
    address = models.TextField()

class PersonModel():
    name = models.TextField()
    surname = models.TextField()
    middlename = models.TextField()
    birthdate = models.TextField()

class PlaceModel():
    name = models.TextField()
    description = models.TextField()
    category = models.TextField()
    picture = models.TextField()
    Address = models.ForeignKey(AddressModel)
    Location = models.ForeignKey(LocationModel)

class ProductModel():
    name = models.TextField()
    description = models.TextField()
    category = models.TextField()
    picture = models.TextField()
    Company = models.ForeignKey(OrganizationModel)
    year = models.TextField()

class ServiceModel():
    name = models.TextField()
    description = models.TextField()
    category = models.TextField()
    picture = models.TextField()
    Company = models.ForeignKey(OrganizationModel)
    year = models.TextField()

class GenericModel(OpeniContextAwareModel):
    # id is missing because it is the default
    url = models.TextField()
    object_type = models.TextField()
    service = models.TextField()
    From = models.ForeignKey(FromModel)
    Time = models.ForeignKey(TimeModel)