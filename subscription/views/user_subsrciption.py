import datetime

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from subscription.permissions import IsOwnerOrReadOnly
from subscription.serializers import SubscriptionSerializer
from subscription.models import Subscription


class UserSubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'product_id'
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user, status=True)

    def get_object(self):
        queryset = self.get_queryset().filter(product_id=self.kwargs[self.lookup_field])

        obj = get_object_or_404(queryset)

        return obj

    def get(self, request, *args, **kwargs):
        # if product_id is None:
        #     return Response({"message": "product_id parametresi eksik"})
        # self.get_queryset().filter(product_id=product_id)
        obj = self.get_object()
        if obj.end_date < datetime.date.today():
            obj.status = False
            obj.save()
            return Response({"message": "Üyeliğinizin süresi doldu."})
        return super(UserSubscriptionDetail, self).get(request, *args, **kwargs)


class UserSubscriptionList(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)
