
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from category.models import Cart, CartItem, Category, Product
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
       'newProducts':newProducts,
    });


def product_search(request):
    query = request.GET.get('q')
    categories = Category.objects.annotate(product_count=Count('products'))
    products = Product.objects.all()
    newProducts = Product.objects.order_by('-created_at')[:5]

    if query:
        products = products.filter(name__icontains=query)

    paginator = Paginator(products, 8)  # Show 8 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    return render(request, 'product.html', {
        'page_obj': page_obj,
        'categories': categories,
        'query': query,
        'newProducts':newProducts
    })

def get_user_cart(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart
@login_required
def add_to_cart(request, product_id,quantity=1):
    quantity=request.GET.get('quantity')
    if not request.user.is_authenticated:
        return redirect('accounts:login')  # Redirect to login if user is not authenticated
    product = get_object_or_404(Product, id=product_id)
    cart = get_user_cart(request.user)

    # Check if the product already exists in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += quantity  # Increment quantity if the item already exists
    cart_item.save()

    return redirect('home:view_cart')

def remove_from_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    cart = get_user_cart(request.user)
    cart_item = cart.items.filter(product_id=product_id).first()
    if cart_item:
        cart_item.delete()

    return redirect('home:view_cart')

def update_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    quantity = request.POST.get('quantity')
    cart = get_user_cart(request.user)
    cart_item = cart.items.filter(product_id=product_id).first()
    if cart_item:
        cart_item.quantity = quantity
        cart_item.save()

    return redirect('home:view_cart')


def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    cart = get_user_cart(request.user)
    items = cart.items.all()
    total_price = sum(item.product.price * item.quantity for item in items)

    return render(request, 'cart.html', {'cart_items': items, 'total_price': total_price})