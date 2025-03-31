from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group
from .forms import ReviewForm
from .models import Tovars, Review
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
