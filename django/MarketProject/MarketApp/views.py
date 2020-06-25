from django.shortcuts import render, HttpResponse
from MarketApp.models import Markets, Products, Cart, History_Carts
from django.db.models import Max

# Create your views here.
def home(request):
    all_markets = Markets.objects.all()
    return render(request, "MarketApp/home.html", {"markets": all_markets})

def markets(request):
    return render(request, "MarketApp/markets.html")

def products(request, market):
    market_Name = market

    if market != 'None':
        all_products = Products.objects.filter(market=market)
        selected_Market = Markets.objects.get(id=market)
        market_Name = selected_Market.name + ' ' +  selected_Market.place
    else:
        all_products = Products.objects.all()

    return render(request, "MarketApp/products.html", {"products": all_products, "marketName": market_Name})

def cart(request, clickedProduct, mode):
    if clickedProduct != 'None':
        if mode == 'add':
            row = Cart(product_id=clickedProduct)
            row.save()
        elif mode == 'delete':
            Cart.objects.filter(id=clickedProduct).delete()
    elif mode == 'delete_all':
        nextId = History_Carts.objects.aggregate(Max('idCart'))['idCart__max'] +1
        all_products = Cart.objects.all()
        for a in all_products:
            row = History_Carts(idCart=nextId, nameProduct=a.product.name, nameMarket=a.product.market.name, priceProduct=a.product.price)
            row.save()
        Cart.objects.filter().delete()
   
    all_products = Cart.objects.all()
    total = 0
    for p in all_products:
        total += p.product.price

    return render(request, "MarketApp/cart.html", {"products": all_products, "total": round(total, 2)})

def historyCarts(request):
    
    return render(request, "MarketApp/historyCarts.html")