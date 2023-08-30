from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Account(models.Model):
    name = models.CharField(max_length=64)
    phone_number = PhoneNumberField(max_length=16)
    email = models.EmailField(max_length=64)

    def __str__(self):
        return self.name


class Leak(models.Model):
    name = name = models.CharField(max_length=64)
    phone_number = PhoneNumberField(max_length=16)
    account = models.ForeignKey("base.Account",
                                on_delete=models.CASCADE,
                                related_name="leak"
                                )

    def __str__(self):
        return self.name
