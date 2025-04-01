from django.contrib import admin
from django.urls import path
from comments import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('tovar/<int:tovar_id>/', views.tovar_detail, name='tovar_detail'),
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.Cart_page, name='cart'),
    path('add_to_cart/<int:tovar_id>/', views.add_to_cart, name='add_to_cart'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)