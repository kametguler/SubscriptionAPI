from subscription.models import Subscription
from rest_framework import serializers
from subscription.serializers.product import ProductSerializer


class SubscriptionSerializer(serializers.ModelSerializer):
    software = ProductSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'software', 'start_date', 'end_date', 'price_paid', 'status']
