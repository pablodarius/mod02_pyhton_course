from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "MarketApp/home.html")

def markets(request):
    return render(request, "MarketApp/markets.html")

def cart(request):
    return render(request, "MarketApp/cart.html")

def products(request):
    return render(request, "MarketApp/products.html")
