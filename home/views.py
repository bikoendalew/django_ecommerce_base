from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from category.models import Category, Product
from django.db.models import Count


# Create your views here.

def home(request):
    newProducts = Product.objects.order_by('-created_at')[:5]
    categories = Category.objects.annotate(product_count=Count('products'))
    products = Product.objects.all()# Fetch all products
    paginator = Paginator(products, 4)  # Show 4 products per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  

    return render(request,'body.html',{
       'categories':categories,
       'page_obj':page_obj,
       'newProducts':newProducts
    });

def product(request):
    products=Product.objects.all()
    categories = Category.objects.annotate(product_count=Count('products'))
    newProducts = Product.objects.order_by('-created_at')[:5]
    products = Product.objects.all()# Fetch all products
    paginator = Paginator(products, 4)  # Show 4 products per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  

    return render(request,'product.html',{
       'categories':categories,
       'page_obj':page_obj,
       'newProducts':newProducts
    });

def product_by_category(request, cat_slug):
       
    category = get_object_or_404(Category, slug=cat_slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.annotate(product_count=Count('products'))
    paginator = Paginator(products, 4)  # Show 4 products per page
    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number) 
    newProducts = Product.objects.order_by('-created_at')[:5]
    return render(request,'product.html',{
       'categories':categories,
       'page_obj':page_obj,
       'newProducts':newProducts
    });