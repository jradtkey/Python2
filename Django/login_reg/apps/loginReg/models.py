from __future__ import unicode_literals
import re, md5, bcrypt
password = 'password'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        users = User.objects.filter(email=postData['email'])
        errors = {}
        if len(postData['first_name']) < 3:
            errors["first_name"] = "First name cannot be fewer than 2 characters."
        firstName = postData['first_name']
        lastName = postData['last_name']
        if not firstName.isalpha() or not lastName.isalpha():
            errors["first_name"] = "First and last name can only contain letters."
        if len(postData['last_name']) < 3:
            errors["last_name"] = "Last name cannot be fewer than 2 characters."
        if len(users) > 0:
            errors["email"] = "Email already exists."
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email."
        if len(postData['password']) < 9:
            errors["password"] = "Password must be longer than 8 characters."
        if postData['password'] != postData['confirm']:
            errors["passowrd"] = "Passwords do not match."
        return errors;

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)

    objects = UserManager()
