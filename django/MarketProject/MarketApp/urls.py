from django.urls import path
from MarketApp import views

urlpatterns = [    
    path('', views.home, name="Home"),
    path('markets', views.markets, name="Markets"),
    path('cart', views.cart, name="Cart"),
    path('products', views.products, name="Products"),    
]