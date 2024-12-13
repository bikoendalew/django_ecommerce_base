from . import views
from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
