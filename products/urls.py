from django.urls import path

from .views import ProductList, add_to_cart, delete_from_cart, CartPage, OrdersPage, make_order, search_view


urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('cart/', CartPage.as_view(), name='cart'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add_product'),
    path('delete-from-cart/<int:pk>/', delete_from_cart, name='delete_from_cart'),
    path('my-orders', OrdersPage.as_view(), name='orders'),
    path('make-order/', make_order, name='do_order'),
    path('search/', search_view, name='search')
]

app_name = 'products'
