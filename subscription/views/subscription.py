from rest_framework import generics, permissions
from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer
from subscription.permissions import IsOwnerOrReadOnly


class SubscriptionList(generics.ListCreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)


class SubscriptionDetail(generics.RetrieveDestroyAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)
