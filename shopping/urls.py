from shopping.views import AddToCartView, OrderItemDeleteView, Cart, CheckoutView
from django.urls import path

urlpatterns = [
    path("sepete-ekle/<int:product_id>/", AddToCartView.as_view(), name='add-to-cart'),
    path("sepetten-kaldir/<int:product_id>/", OrderItemDeleteView.as_view(), name='remove-from-cart'),
    path("sepetim/", Cart.as_view(), name='cart-list'),
    path("odeme/", CheckoutView.as_view(), name='checkout'),
]
