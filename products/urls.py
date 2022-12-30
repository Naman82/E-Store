from django.urls import path
from . import views as productview

urlpatterns=[
    path('product/',productview.ProductView.as_view(),name="product"),
    path('category/',productview.CategoryView.as_view(),name="category"),
    path('inventory/',productview.InventoryView.as_view(),name="inventory"),
    path('discount/',productview.DiscountView.as_view(),name="discount"),
]