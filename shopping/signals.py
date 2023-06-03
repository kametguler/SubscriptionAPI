from datetime import timedelta
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from subscription.models import Subscription, Product  # Örnek olarak User modelini kullanıyoruz
from shopping.models import Order, OrderItem  # Güncellenen modelinizi burada import edin


@receiver(post_save, sender=Order)  # Güncellenen modeli belirtin
def create_subs_model(sender, instance, created, **kwargs):
    if not created:
        if instance.status == "delivered":
            try:
                order_items = OrderItem.objects.filter(order=instance)
                bought_products = []
                for order_item in order_items:
                    if order_item.price == order_item.product.price_yearly:
                        bought_products.append(
                            {"product_id": order_item.product.id, "date": 365, "price": order_item.price})
                    elif order_item.price == order_item.product.price_6months:
                        bought_products.append(
                            {"product_id": order_item.product.id, "date": 180, "price": int(order_item.price)})
                    else:
                        bought_products.append(
                            {"product_id": order_item.product.id, "date": 30, "price": order_item.price})

                for bought in bought_products:
                    Subscription.objects.create(user=instance.user,
                                                product_id=bought["product_id"],
                                                start_date=now(),
                                                end_date=now() + timedelta(days=bought["date"]),
                                                price_paid=bought["price"],
                                                status=True).save()
                print(bought_products)
            except Exception as E:
                print(E)
