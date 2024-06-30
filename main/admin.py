from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import RentPlace, BaseUser, WeaponApplication


@admin.register(WeaponApplication)
class WeaponApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'weapon_type', 'comment', 'application_date')
    search_fields = ('user__username', 'weapon_type')
    list_filter = ('weapon_type', 'application_date')
    readonly_fields = ('user', 'application_date')

    fieldsets = [
        ('Основная информация', {'fields': ['user', 'weapon_type', 'reason']}),
        ('Дополнительная информация', {'fields': ['application_date']}),
    ]


@admin.register(RentPlace)
class RentPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',  'inhabiants', 'price', 'place_type')
    search_fields = ('name', 'location', 'inhabiants')
    list_filter = ('place_type',)
    ordering = ('name',)


@admin.register(BaseUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'otchestvo', 'have_licence')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Products', {'fields': ('buyed_products', 'cart')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'otchestvo', 'have_licence'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'have_licence')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'otchestvo')
    ordering = ('username',)

