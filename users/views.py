from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from drf_social_oauth2.views import TokenView, ConvertTokenView
from EStoreBackend.utils import send_response
from social_django.models import UserSocialAuth
from django.contrib.auth.models import User
# Create your views here.

# @method_decorator(name='post', decorator=swagger_auto_schema(
#     operation_description="Authenticate the user",
#     tags=["User Authentication"],
#     request_body=openapi.Schema(
#         type=openapi.TYPE_OBJECT,
#         properties={
#             'client_id':openapi.Schema(type=openapi.TYPE_STRING),
#             'client_secret':openapi.Schema(type=openapi.TYPE_STRING),
#             'grant_type':openapi.Schema(type=openapi.TYPE_STRING),
#             'username':openapi.Schema(type=openapi.TYPE_STRING),
#             'password':openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD)
#         }
#     )
# ))
# class LoginToken(APIView):
#     def post(request):
#         pass
@method_decorator(name='post', decorator=swagger_auto_schema(
    operation_description="Save User Details",
    tags=["User Authentication"],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'first_name':openapi.Schema(type=openapi.TYPE_STRING),
            'last_name':openapi.Schema(type=openapi.TYPE_STRING),
            'email':openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL),
            'password':openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD)
        }
    )
))
class UserRegisterView(APIView):
    def post( self,request):
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        try:
            # print(first_name,last_name,email,password)
            if first_name is not None and last_name is not None and email is not None and password is not None:
                user = User.objects.filter(email=email)
                if not user.exists():
                    User.objects.create_user(username=email, email=email, first_name=first_name, last_name=last_name, password=password,)
                    return send_response(result=True, message="User created successfully")
                else:
                    if UserSocialAuth(user=user[0]).user_exists():
                        return send_response(result=False, message="Please login using socials")
                    return send_response(result=False, message="User with this email already exists")
            else:
                return send_response(result=False, message="Empty Fields")     
        except Exception as e:
            return send_response(result=False, message=str(e))


@method_decorator(name="post", decorator=swagger_auto_schema(
     operation_description="Test for login",
    tags=["User Authentication"],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'client_id': openapi.Schema(type=openapi.TYPE_STRING, description="Client Id (Casa Arch)"),
            'client_secret': openapi.Schema(type=openapi.TYPE_STRING, description="Client Secret (Casa Arch)"),
            'grant_type':openapi.Schema(type=openapi.TYPE_STRING, description="Should be 'password' ",),
            'username':openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL, description="Username (Email)"),
            'password':openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD, description="Password")
        }
    ),
))
class TokenViewNew(TokenView):
    pass

@method_decorator(name="post", decorator=swagger_auto_schema(
     operation_description="Test for login",
    tags=["User Authentication"],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'client_id': openapi.Schema(type=openapi.TYPE_STRING, description="Client Id (Casa Arch)"),
            'client_secret': openapi.Schema(type=openapi.TYPE_STRING, description="Client Secret (Casa Arch)"),
            'grant_type':openapi.Schema(type=openapi.TYPE_STRING, description="Should be 'convert_token' ",),
            'backend':openapi.Schema(type=openapi.TYPE_STRING, description="'facebook' for facebook, 'google-oauth2' for google"),
            'token':openapi.Schema(type=openapi.TYPE_STRING, description="token"),
        }
    ),
))
class convertTokenViewNew(ConvertTokenView):
    pass