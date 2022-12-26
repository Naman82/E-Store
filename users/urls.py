from django.urls import path
from . import views as userView
urlpatterns=[
    path('user-register',userView.UserView.as_view(),name='userRegister'),
    path('user-login', userView.TokenViewNew.as_view(), name='token'),
    path('user-convert-token', userView.convertTokenViewNew.as_view(), name='convert-token'),
    path('profile-pic/',userView.ProfilePicView.as_view(),name="profile-pic"),
    path('customer-profile/',userView.CustomerProfileView.as_view(),name="customer-profile"),
    path('seller-profile/',userView.SellerProfileView.as_view(),name="seller-profile"),
]