from django.urls import path
from MarketApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('', views.home, name="Home"),
    path('markets', views.markets, name="Markets"),
    path('cart/<clickedProduct>/<mode>', views.cart, name="Cart"),
    path('products/<market>', views.products, name="Products"),
    path('historyCarts', views.historyCarts, name="HistoryCarts"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
