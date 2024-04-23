from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Cart
from django.contrib.auth.models import User
from .forms import UsernameForm, PasswordForm

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products, 'user': request.user})      

def car_detail(request, car_id):
    car = get_object_or_404(Product, pk=car_id)
    return render(request, 'detail.html', {'car':car})

def contact(request):
    return render (request, 'contact.html')

def cart(request):
    products = Product.objects.all()
    return render(request,'cart.html',{'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # Perform any logic to add the product to the cart
    # For example, you can create a Cart object and add the product to it
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    return redirect('cart')  # Redirect to the cart page after adding the product


def username_page(request):
    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                request.session['username'] = username
                return redirect('password_page')
            else:
                return redirect('signup_page')
    else:
        form = UsernameForm()
    return render(request, 'registration/username_page.html', {'form': form})

def password_page(request):
    if 'username' in request.session:
        username = request.session['username']
        print("Username from session:", username)  # Add this line for debugging
        if request.method == 'POST':
            form = PasswordForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    print("User authenticated successfully:", user)  # Add this line for debugging
                    login(request, user)
                    return redirect('index')
        else:
            # Display authenticated username with an option to edit
            form = PasswordForm(initial={'username': username})
        return render(request, 'registration/password_page.html', {'form': form, 'authenticated_username': username})
    else:
        return redirect('username_page')


def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup_page.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')
