from django.contrib import admin
from .models import Product, Variation

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'slug', 'is_available',
                    'stock', 'created_date', 'modified_date')


admin.site.register(Product, ProductAdmin),

admin.site.register(Variation)
