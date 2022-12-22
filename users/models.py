from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

import os, uuid

from .managers import UserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    def get_update_filename(self, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('uploads/user/profile', filename)
    username = None
    USER_TYPE_CHOICES = [
        (0, 'Admin'),
        (1, 'Professional'),
        (2, 'Customer'),
    ]
    email = models.EmailField(_('email address'), unique=True, null=True)
    email_verified = models.BooleanField(default=False)
    type = models.IntegerField(choices=USER_TYPE_CHOICES, default=2)
    date_joined = models.DateTimeField(default=timezone.now)
    phone=models.PositiveBigIntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    profile_pic = models.ImageField(upload_to=get_update_filename, default='uploads/user/profile/default_profile.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['type']
    object = UserManager()

    def __str__(self):
        return "{},{},{}".format(self.email, self.first_name, self.type_value)

    def get_user_type(self):
        return self.type

    @property
    def type_value(self):
        return dict(self.USER_TYPE_CHOICES)[self.type]

class CustomerProfile(models.Model):
    GENDER = [
        (0,'Male'),
        (1,'Female'),
        (2,'Other')
    ]
    user=models.ForeignKey("users.User",on_delete=models.CASCADE)
    country=models.CharField(max_length=255,null=True,blank=True)
    state=models.CharField(max_length=255,null=True,blank=True)
    city=models.CharField(max_length=255,null=True,blank=True)
    gender=models.IntegerField(choices=GENDER,default=0)
    pincode=models.PositiveIntegerField(null=True,blank=True)
    address=models.CharField(max_length=255,null=True,blank=True)
    age=models.PositiveIntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

    @property
    def gender_value(self):
        return dict(self.GENDER)[self.gender]


class SellerProfile(models.Model):
    GENDER = [
        (0,'Male'),
        (1,'Female'),
        (2,'Other')
    ]
    user=models.ForeignKey("users.User",on_delete=models.CASCADE)
    country=models.CharField(max_length=255,null=True,blank=True)
    state=models.CharField(max_length=255,null=True,blank=True)
    city=models.CharField(max_length=255,null=True,blank=True)
    pincode=models.PositiveIntegerField(null=True,blank=True)
    address=models.CharField(max_length=255,null=True,blank=True)
    gender=models.IntegerField(choices=GENDER,default=0)
    age=models.PositiveIntegerField(blank=True,null=True)
    is_business = models.BooleanField(default=False)
    business_website = models.URLField(null=True,blank=True)
    business_name = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

    @property
    def gender_value(self):
        return dict(self.GENDER)[self.gender]