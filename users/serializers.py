from rest_framework import serializers
from .models import User,CustomerProfile,SellerProfile

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['profile_pic',]

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CustomerProfile
        fields="__all__"

class SellerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=SellerProfile
        fields="__all__"