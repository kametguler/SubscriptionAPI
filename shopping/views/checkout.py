from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect, render
from shopping.models import Order, OrderItem, BillingInformation
from shopping.forms import CheckoutForm


class CheckoutView(View):
    def get(self, request):
        order = Order.objects.filter(user=request.user, status='created').first()
        if not order or order.total_amount == 0.00:
            return redirect('cart-list')
        order_items = order.items.all()
        form = CheckoutForm()
        context = {
            'form': form,
            'order': order,
            'order_items': order_items
        }
        return render(request, 'shop/checkout.html', context)

    def post(self, request):
        order = Order.objects.filter(user=request.user, status='created').first()
        if not order or order.total_amount == 0.00:
            return redirect('home')

        form = CheckoutForm(request.POST)
        if form.is_valid():
            billing_info = BillingInformation(
                order=order,
                full_name=form.cleaned_data['full_name'],
                email=request.user.email,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                postal_code=form.cleaned_data['postal_code'],
            )
            billing_info.save()

            # Set order status to 'processing'
            order.status = 'pending'
            order.save()

            # Redirect to home page
            return redirect('shop')
        order_items = order.items.all()
        context = {
            'form': form,
            'order': order,
            'order_items': order_items
        }
        return render(request, 'shop/checkout.html', context)
