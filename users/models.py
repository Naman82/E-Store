from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AppUser(models.Model):
    USER_TYPE_CHOICES = [
        ('S', 'Seller'),
        ('C', 'Customer'),
    ]

    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]


    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="appuser")
    user_type=models.CharField(max_length=1,choices=USER_TYPE_CHOICES,default='C')
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    mobile =models.PositiveIntegerField(null=True, blank=True)
    address=models.CharField(max_length=500, null=True, blank=True)
    city=models.CharField(max_length=250, null=True, blank=True)
    pincode=models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return self.user.username
    
