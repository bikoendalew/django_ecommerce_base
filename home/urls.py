
from . import views
from django.contrib import admin
from django.urls import include, path


app_name = 'home'

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.product,name='product'),
    path('category/<slug:cat_slug>/', views.product_by_category, name='Pcategory'),
    path('search/', views.product_search, name='product_search'),
 

    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:product_id>/', views.update_cart, name='update_cart_quantity'),
]
