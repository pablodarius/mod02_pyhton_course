from django.shortcuts import render, HttpResponse
from MarketApp.models import Markets, Products

# Create your views here.
def home(request):
    all_markets = Markets.objects.all()
    return render(request, "MarketApp/home.html", {"markets": all_markets})

def markets(request):
    return render(request, "MarketApp/markets.html")

def cart(request):
    return render(request, "MarketApp/cart.html")

def products(request, market):    
    market_Name = market

    if market != 'None':
        all_products = Products.objects.filter(market=market)
        selected_Market = Markets.objects.get(id=market)
        market_Name = selected_Market.name + ' ' +  selected_Market.place
    else:
        all_products = Products.objects.all()
        
    return render(request, "MarketApp/products.html", {"products": all_products, "marketName": market_Name})
