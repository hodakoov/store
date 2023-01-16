from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Product, ProductCategory, Baskets
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page_number=1):
    products = Product.objects.filter(category__id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
    }
    return render(request, 'products/products.html', context)


@login_required
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


@login_required
def basket_remove(request, basket_id):
    basket = Baskets.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

