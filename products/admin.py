from django.contrib import admin
from .models import Product, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'datetime_made')
    list_display_links = ('pk',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color', 'producer_country')
    search_fields = ('name', 'desc', 'producer_country')
    list_filter = ('color', 'producer_country')
    ordering = ('name',)

