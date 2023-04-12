from allauth.account.views import PasswordChangeView
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from shopping.models import Order
from subscription.models import Subscription
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, View):
    redirect_field_name = reverse_lazy("account_login")

    def get(self, *args, **kwargs):
        return render(self.request, 'profiles/profiles.html', context={})


class SubscriptionsView(LoginRequiredMixin, View):
    redirect_field_name = reverse_lazy("account_login")

    def get(self, *args, **kwargs):
        user = self.request.user
        subscriptions = Subscription.objects.filter(status=True, user=user)
        context = {
            "subscriptions": subscriptions
        }
        return render(self.request, 'profiles/subscriptions.html', context=context)


class OrdersView(LoginRequiredMixin, View):
    redirect_field_name = reverse_lazy("account_login")

    def get(self, *args, **kwargs):
        user = self.request.user
        orders = Order.objects.filter(user=user).exclude(status='created')
        context = {
            "orders": orders
        }
        return render(self.request, 'profiles/orders.html', context=context)

