from django.db import models
from django.contrib.auth.models import User
from subscription.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email + " " + self.product

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'product'], name='unique_cart_item'),
        ]


class Cities(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField()

    def __str__(self):
        return f"{str(self.code)} - {self.name}"
