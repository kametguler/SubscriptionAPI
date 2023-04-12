from django.db import models
from django.contrib.auth.models import User
from subscription.models import Product

ORDER_STATUS_CHOICES = (
    ('created', 'Sepet'),
    ('pending', 'Ödeme Bekleniyor'),
    ('shipped', 'Kargoya Verildi'),
    ('delivered', 'Teslim Edildi'),
    ('cancelled', 'İptal Edildi'),
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES)

    def __str__(self):
        return self.user.email + " " + str(self.total_amount) + "₺"

    def update_total_amount(self):
        self.total_amount = sum(item.price * item.quantity for item in self.items.all())
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.price) + " " + self.product.name

    def save(self, *args, **kwargs):
        super(OrderItem, self).save(*args, **kwargs)
        self.order.update_total_amount()


class BillingInformation(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="Türkiye")
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name
