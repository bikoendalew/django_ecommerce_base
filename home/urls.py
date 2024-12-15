
from . import views
from django.contrib import admin
from django.urls import include, path


app_name = 'home'

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.product,name='product'),
    path('category/<slug:cat_slug>/', views.product_by_category, name='Pcategory'),
    path('search/', views.product_search, name='product_search'),
 
]
