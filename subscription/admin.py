from django.contrib import admin
from subscription.models import Subscription, Product, ProductFeedback

admin.site.register(Subscription)
admin.site.register(Product)
admin.site.register(ProductFeedback)
