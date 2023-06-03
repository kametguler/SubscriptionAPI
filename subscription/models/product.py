from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_monthly = models.DecimalField(max_digits=10, decimal_places=2)
    price_6months = models.DecimalField(max_digits=10, decimal_places=2)
    price_yearly = models.DecimalField(max_digits=10, decimal_places=2)
    discount_rate = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    unique_name = models.CharField(unique=True, blank=True, null=True, max_length=255)
    installation = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductFeedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedbacks')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField()
    allowed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - {self.customer.email} ({str(self.rating)} stars)"
