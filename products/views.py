from typing import Any

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db import models
from django.http import HttpResponse
from django.db.models.aggregates import Sum

from .models import Product, Order, RentOrder


class ProductList(ListView):
    template_name = 'products/products.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


def add_to_cart(request, pk: int):
    product = Product.objects.get(pk=pk)

    if request.user.is_authenticated:
        request.user.cart.add(product)
        request.user.save()

        return redirect('products:cart')
    else:
        return redirect('main:login')


def delete_from_cart(request, pk: int):
    product = Product.objects.get(pk=pk)

    if request.user.is_authenticated:
        request.user.cart.remove(product)
        request.user.save()

        return redirect('products:cart')
    else:
        return redirect('main:home')


class CartPage(ListView):
    context_object_name = 'products'
    template_name = 'products/cart.html'

    def get_queryset(self) -> models.QuerySet[Any]:
        if self.request.user.is_authenticated:
            return self.request.user.cart.all()
        else:
            return None


class OrdersPage(ListView):
    context_object_name = 'orders'
    template_name = 'products/orders.html'

    def get_queryset(self) -> models.QuerySet[Any]:
        if self.request.user.is_authenticated:
            return Order.objects.filter(user=self.request.user).annotate(total_price=Sum('products__price'))
        else:
            return None
        
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['places'] = RentOrder.objects.filter(user=self.request.user)

        return context


def make_order(request):
    if request.user.is_authenticated:
        cart_products = request.user.cart.all()

        if len(cart_products) == 0:
            return redirect('products:cart')
        
        order = Order.objects.create(user=request.user)
        order.products.add(*cart_products)
        order.save()

        return redirect('products:orders')
    else:
        return HttpResponse('Unauthtorized', status=401)


def search_view(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__regex=r'(?i){}'.format(query)) if query else []

    return render(request, 'products/products.html', {'products': products})
