from enum import Enum
from django.db import models




class Address(models.Model):
    street = models.CharField(max_length=40)
    street_number = models.CharField(max_length=10)
    city_code = models.CharField(max_length=5)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=40)


class AppUser(models.Model):
    MALE = "MALE"
    FEMALE = "FEMALE"
    UNSET = "UNSET"
    GENDER_CHOICES = {
        MALE: "Male",
        FEMALE: "Female",
        UNSET: "Unset",
    }

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, default=UNSET)
    customer_id = models.UUIDField()
    phone_number = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    address_id = models.ForeignKey(Address, on_delete=models.PROTECT)
    birthday = models.DateField()
    last_updated = models.DateField(auto_now=True)


class CustomerRelationship(models.Model):
    appuser_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    points = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField()
