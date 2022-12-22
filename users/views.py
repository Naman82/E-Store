from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from social_django.models import UserSocialAuth
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from drf_social_oauth2.authentication import SocialAuthentication
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import UserProfileSerializer
from .models import User
from EStoreBackend.utils import send_response
from drf_social_oauth2.views import TokenView, ConvertTokenView
image_id = openapi.Parameter('id', openapi.IN_QUERY, description="Id of object to delete", type=openapi.TYPE_INTEGER)




@method_decorator(name='post', decorator=swagger_auto_schema(
    operation_description="Save User Details",
    tags=["User Authentication"],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'first_name':openapi.Schema(type=openapi.TYPE_STRING),
            'last_name':openapi.Schema(type=openapi.TYPE_STRING),
            'email':openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL),
            'password':openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD),
            'phone':openapi.Schema(type=openapi.TYPE_INTEGER,description="optional")
        }
    )
))
class UserView(APIView):

    def post(self, request):
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        try:
            print(first_name,last_name,email,password)
            if first_name is not None and last_name is not None and email is not None and password is not None:
                user = User.object.filter(email=email)
                if not user.exists():
                    User.object.create_user(email=email, first_name=first_name, last_name=last_name, password=password,)
                    # obj=[email,first_name,last_name]
                    # send_welcome_mail_customer(obj)
                    return send_response(result=True, message="User created successfully")
                else:
                    if UserSocialAuth(user=user[0]).user_exists():
                        return send_response(result=False, message="Please login using socials")
                    return send_response(result=False, message="User with this email already exists")
            else:
                return send_response(result=False, message="Empty Fields")
        except Exception as e:
            return send_response(result=False, message=str(e))

# USER DETAILS

@method_decorator(name='patch', decorator=swagger_auto_schema(
    operation_description="Save User Details",
    tags=["User Details"],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
    )
))
class ProfilePicView(APIView):

    permission_classes=[IsAuthenticated]
    authentication_classes=[OAuth2Authentication,SocialAuthentication]
    parser_classes=[FormParser,MultiPartParser]

    def patch(self,request):
        try:
            user=User.objects.get(pk=request.user.pk)
            userProfile=UserProfileSerializer(user,data=request.data)
            if userProfile.is_valid():
                userProfile.save()
                return send_response(result=True,message="Profile Picture updated successfully")
            else:
                return send_response(result=False,message="Something went wrong! Try again")
        except Exception as e:
            return send_response(result=False, message=str(e))
            

# AUTHENTICATION EXTENDED VIEWS
@method_decorator(name="post", decorator=swagger_auto_schema(
     operation_description="Test for login",
    tags=["User Authentication"],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'client_id': openapi.Schema(type=openapi.TYPE_STRING, description="Client Id (E-Store)"),
            'client_secret': openapi.Schema(type=openapi.TYPE_STRING, description="Client Secret (E-Store)"),
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
            'client_id': openapi.Schema(type=openapi.TYPE_STRING, description="Client Id (E-Store)"),
            'client_secret': openapi.Schema(type=openapi.TYPE_STRING, description="Client Secret (E-Store)"),
            'grant_type':openapi.Schema(type=openapi.TYPE_STRING, description="Should be 'convert_token' ",),
            'backend':openapi.Schema(type=openapi.TYPE_STRING, description="'facebook' for facebook, 'google-oauth2' for google"),
            'token':openapi.Schema(type=openapi.TYPE_STRING, description="token"),
        }
    ),
))
class convertTokenViewNew(ConvertTokenView):
    pass