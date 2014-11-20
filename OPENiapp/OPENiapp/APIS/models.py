from datetime import datetime

from django.db import models

from OPENiapp.APIS.Context.models import OpeniContextAwareModel

#   Set of Properties
class AddressModel(models.Model):
    street = models.TextField()
    number = models.TextField()
    apartment = models.TextField()
    city = models.TextField()
    locality = models.TextField()
    country = models.TextField()
    zip = models.TextField()


class TimeModel(models.Model):
    created_time = models.TextField()
    edited_time = models.TextField()
    deleted_time = models.TextField()

    def __unicode__(self):
        return "%s" % (self.created_time)


class DurationModel(models.Model):
    starts_time = models.TextField()
    ends_time = models.TextField()


class FromModel(models.Model):
    from_id = models.TextField(blank=True, null=True)
    object_type = models.TextField()
    url = models.TextField()
    name = models.TextField()

    def __unicode__(self):
        return "%s" % (self.from_id)


class LocationModel(models.Model):
    latitude = models.TextField()
    longitude = models.TextField()
    height = models.TextField()


class SizeModel(models.Model):
    depth = models.TextField()
    height = models.TextField()
    width = models.TextField()


class TagsModel(models.Model):
    tag_id = models.TextField()
    name = models.TextField()
    Time = models.ForeignKey(TimeModel)
    x_location = models.TextField()
    y_location = models.TextField()


class ApplicationModel(models.Model):
    title = models.TextField()
    description = models.TextField()
    version = models.TextField()
    icon = models.TextField()
    developer = models.TextField()


class BaseFileModel(models.Model):
    title = models.TextField()
    description = models.TextField()
    format = models.TextField()
    size = models.TextField()
    icon = models.TextField()


class OrganizationModel(models.Model):
    name = models.TextField()
    description = models.TextField()
    founded = models.TextField()
    address = models.TextField()


class PersonModel(models.Model):
    name = models.TextField()
    surname = models.TextField()
    middlename = models.TextField()
    birthdate = models.TextField()


class PlaceModel(models.Model):
    name = models.TextField()
    description = models.TextField()
    category = models.TextField()
    picture = models.TextField()
    Address = models.ForeignKey(AddressModel)
    Location = models.ForeignKey(LocationModel)


class ProductModel(models.Model):
    name = models.TextField()
    description = models.TextField()
    category = models.TextField()
    picture = models.TextField()
    Company = models.ForeignKey(OrganizationModel)
    year = models.TextField()


class ServiceModel(models.Model):
    name = models.TextField()
    description = models.TextField()
    category = models.TextField()
    picture = models.TextField()
    Company = models.ForeignKey(OrganizationModel)
    year = models.TextField()


class GenericModel(OpeniContextAwareModel):
    url = models.TextField()
    object_type = models.TextField()
    service = models.TextField()
    From = models.ForeignKey(FromModel, default=lambda: FromModel.objects.create(from_id="sample"))
    Time = models.ForeignKey(TimeModel, default=lambda: TimeModel.objects.create(created_time=str(datetime.now())))

    class Meta:
        abstract = True