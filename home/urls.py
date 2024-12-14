
from . import views
from django.contrib import admin
from django.urls import include, path


app_name = 'home'

urlpatterns = [
    path('',views.home,name='home'),
    path('/products',views.product,name='product')
]
