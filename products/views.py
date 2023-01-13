from itertools import product

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Product, ProductCategory, Baskets


def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Baskets.objects.filter(product=product, user=request.user)

    if not baskets.exists():
        Baskets.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Baskets.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

