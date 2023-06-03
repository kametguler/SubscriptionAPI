from django.http import JsonResponse
from django.views.generic import View, ListView
from django.shortcuts import get_object_or_404
from shopping.models import Order, OrderItem
from subscription.models import Product, Subscription


class AddToCartView(View):
    def post(self, request, product_id):
        price_type = request.POST.get('price_type', None)
        if not request.user.is_authenticated:
            return JsonResponse({
                "status": "error", "message": "Sepete ürün ekleyebilmek için giriş yapmalısınız."
            })
        if price_type is not None:
            product = get_object_or_404(Product, pk=product_id)
            if product.discount_rate is not 0:
                if price_type == 'price_monthly':
                    price = product.price_monthly - product.discount_rate
                elif price_type == 'price_6months':
                    price = product.price_6months - product.discount_rate
                elif price_type == 'price_yearly':
                    price = product.price_yearly - product.discount_rate
                else:
                    return JsonResponse(
                        {'status': 'error', 'message': 'Ürün sepete eklenemedi. Lütfen daha sonra tekrar deneyin.'})
            else:
                if price_type == 'price_monthly':
                    price = product.price_monthly
                elif price_type == 'price_6months':
                    price = product.price_6months
                elif price_type == 'price_yearly':
                    price = product.price_yearly
                else:
                    return JsonResponse(
                        {'status': 'error', 'message': 'Ürün sepete eklenemedi. Lütfen daha sonra tekrar deneyin.'})
            subscription = Subscription.objects.filter(user=request.user, product=product, status=True).first()
            if subscription is None:
                order, created = Order.objects.get_or_create(user=request.user, status='created')
                order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
                order_item.price = price
                order_item.save()
                return JsonResponse({'status': 'success', 'message': 'Ürün sepete eklendi.'})
            else:
                return JsonResponse(
                    {'status': 'danger', 'message': 'Bu ürüne ait aktif bir aboneliğiniz bulunmaktadır.'})
        else:
            return JsonResponse({'status': 'danger', 'message': 'Lütfen fiyat seçeneği seçin.'})


class OrderItemDeleteView(View):
    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id', None)
        if product_id is not None:
            order = Order.objects.filter(status='created', user=request.user).first()
            delete_item = get_object_or_404(OrderItem, order=order, product_id=product_id)
            order.total_amount -= delete_item.price
            order.save()
            delete_item.delete()
            return JsonResponse({"status": "success", "message": 'Ürün başarıyla kaldırıldı'})
        else:
            return JsonResponse({"status": "danger", "message": 'Ürün silinmek isterken hata'})


class Cart(ListView):
    model = OrderItem
    template_name = 'shop/cart.html'
    context_object_name = 'order_items'

    def get_queryset(self):
        order, created = Order.objects.get_or_create(user=self.request.user, status='created')
        queryset = super().get_queryset()
        order_items = queryset.filter(order=order)
        self.subtotal = order.total_amount
        return order_items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtotal'] = self.subtotal
        return context
