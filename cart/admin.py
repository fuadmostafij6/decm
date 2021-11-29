from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cart, CartItem


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'is_active')


admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)
