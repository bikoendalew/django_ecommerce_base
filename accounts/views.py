from django.shortcuts import render, redirect
from django.contrib.auth import login
from .form import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('shop:product_list')  # Redirect to the product list
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:product_list')  # Redirect to your desired page after login
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid email or password'})
    return render(request, 'accounts/login.html')
