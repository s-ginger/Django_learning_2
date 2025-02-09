from django.contrib import admin
from django.urls import path
from comments import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
]