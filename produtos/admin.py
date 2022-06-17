from django.contrib import admin
from produtos.models import Product

class ProductList(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'available')
    list_filter = ('category',)
    list_editable = ('available',)

admin.site.register(Product, ProductList)