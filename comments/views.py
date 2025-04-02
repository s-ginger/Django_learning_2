from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group
from .forms import ReviewForm
from .models import Tovars, Review, CartItem, Cart
from django.contrib.auth.decorators import login_required

def tovar_detail(request, tovar_id):
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = get_object_or_404(Tovars, pk=tovar_id)
            review.save()
            return redirect('tovar_detail', tovar_id=tovar_id)
    else:
        form = ReviewForm()
    
    tovar = get_object_or_404(Tovars, pk=tovar_id)
    return render(request, 'catalog/tovar_base.html', {
        'tovar': tovar,
        'form': ReviewForm(),  
        'reviews': Review.objects.filter(product=tovar).order_by('-created_at'),  
        })

@login_required
def profile(request):
    reviews = Review.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'comments/profile.html', {'reviews': reviews})

@login_required
def Cart_page(request):
    items = CartItem.objects.filter(user=request.user)  # Получаем все товары в корзине
    total_price = sum(item.products.price * item.quantity for item in items)  # Считаем общую стоимость
    return render(request, 'catalog/cart.html', {'cart_items': items, 'total_price': total_price})


@login_required
def add_to_cart(request, tovar_id):
    tovar = get_object_or_404(Tovars, pk=tovar_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, products=tovar)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('tovar_detail', tovar_id=tovar_id)


def home(request):
    is_admin = request.user.is_authenticated and request.user.groups.filter(name='администраторы').exists()
    all_tovars = Tovars.objects.all()[:10]
    extra_content = "Административный контент" if is_admin else ""
    
    
    return render(request, 'comments/home.html', {
        'tovars': all_tovars,
        'extra_content': extra_content
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
