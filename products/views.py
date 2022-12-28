from django.shortcuts import render
from rest_framework.views import APIView
from users.permissions import SellerUserPermission
from rest_framework.permissions import IsAuthenticated
from EStoreBackend.utils import send_response
from .serializers import ProductSerializer,ProductEditSerializer,CategorySerializer,InventorySerializer,DiscountSerializer
from rest_framework.parsers import FormParser,MultiPartParser
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from drf_social_oauth2.authentication import SocialAuthentication
from .models import Product,Category,Inventory
from users.models import User

# Create your views here.

class ProductView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [OAuth2Authentication,SocialAuthentication]
    parser_classes = [MultiPartParser,FormParser]

    def post(self,request):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return send_response(result=True,message="Product added successfully")
            else:
                return send_response(result=False, message="Invalid Request")
        except Exception as e:
            return send_response(result=False,message=str(e))
    
    def get(self,request):
        try:
            if Product.objects.filter(user=request.user.pk).exists():
                product=Product.objects.filter(user=request.user.pk)
                serializer=ProductSerializer(product)
                return send_response(result=True,data=serializer.data)
            else:
                return send_response(result=False,message="Products for particular Seller does not exist")
        except Exception as e:
            return send_response(result=False,message=str(e))

    def patch(self,request):
        try:
            user=User.objects.get(pk=request.user.pk)
            product = Product.objects.get(pk=request.data.get('product_id'), user=user)
            serializer = ProductEditSerializer(product,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return send_response(result=True,message="Product details editted successfully")
            else:
                return send_response(result=False,message="Invalid Request")
        except Exception as e:
            return send_response(result=False,message=str(e))

    def delete(self,request):
        try:
            product=Product.objects.get(pk=request.data.get('product_id'))
            product.delete()
            return send_response(result=True,message="Product Deleted successfully")
        except Exception as e:
            return send_response(result=False,message=str(e))


class CategoryView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[SocialAuthentication,OAuth2Authentication]
    
    def get(self,request):
        try:
            category=Category.objects.all()
            serialier = CategorySerializer(category)
            return send_response(result=True,data=serialier.data)
        except Exception as e:
            return send_response(result=True,message=str(e))
    
    def post(self,request):
        try:
            serializer=CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return send_response(result=True,message="New Category added")
            else:
                send_response(result=False,message="Invalid Request")
        except Exception as e:
            return send_response(result=False, message=str(e))

class InventoryView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SocialAuthentication,OAuth2Authentication]

    def post(self,request):
        try:
            serializer=InventorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return send_response(result=True,message="Inventory saved successfully")
            else:
                return send_response(result=False,message="Invalid Request")
        except Exception as e:
            return send_response(result=False,message=str(e))

class DiscountView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SocialAuthentication,OAuth2Authentication]

    def post(self,request):
        try:
            serializer=DiscountSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return send_response(result=True,message="Discount saved successfully")
            else:
                return send_response(result=False,message="Invalid Request")
        except Exception as e:
            return send_response(result=False,message=str(e))
            

