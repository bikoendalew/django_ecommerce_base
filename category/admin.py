from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent','created_at')
    search_fields = ('name',)
    ordering = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','price','created_at')
    search_fields=('price','name'),
    ordering= ('name','price')

admin.site.register(Product,ProductAdmin)
admin.site.register(Category, CategoryAdmin)
