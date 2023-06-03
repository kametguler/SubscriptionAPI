from subscription.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price_monthly', 'price_6months', 'price_yearly', 'discount_rate',
                  'status', "unique_name"]
