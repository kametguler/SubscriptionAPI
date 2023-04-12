from django.contrib import admin
from shopping.models import Order, OrderItem, BillingInformation, Cities

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(BillingInformation)
admin.site.register(Cities)
