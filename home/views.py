from django.shortcuts import render

from category.models import Category

# Create your views here.

def home(request):
  
    categories= Category.objects.all()
    return render(request,'body.html',{
       'categories':categories
    });