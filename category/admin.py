from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent','created_at')
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Category, CategoryAdmin)
