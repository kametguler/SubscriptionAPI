from django.contrib.auth.models import User
from django.db import models
from subscription.models import Product


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    session_key = models.CharField(max_length=255, blank=True, null=True)
    price_paid = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
