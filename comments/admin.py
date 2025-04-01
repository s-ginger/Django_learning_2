from django.contrib import admin
from .models import Tovars, Review, Cart, CartItem

admin.site.register(Tovars)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)