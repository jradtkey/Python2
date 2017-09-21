from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['full_name']) < 1:
            errors["full_name"] = "Name cannot be blank."
        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be blank."
        return errors;

class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)

    objects = UserManager()
