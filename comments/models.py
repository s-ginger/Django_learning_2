from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator


    
class Tovars(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Tovars, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5)])
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"