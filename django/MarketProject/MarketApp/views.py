from django.shortcuts import render, HttpResponse
from MarketApp.models import Markets

# Create your views here.
def home(request):
    all_markets = Markets.objects.all()
    return render(request, "MarketApp/home.html", {"markets": all_markets})

def markets(request):
    return render(request, "MarketApp/markets.html")

def cart(request):
    return render(request, "MarketApp/cart.html")

def products(request, market):
    if market != 'None':
        all_products = Markets.objects.filter(name=market)
    else:
        all_products = Markets.objects.all()
        
    return render(request, "MarketApp/products.html", {"products": all_products, "marketName": market})
