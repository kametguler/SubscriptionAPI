from django.urls import path
from subscription.views import ProductListView, ProductDetailView, ContactView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("urunler/", ProductListView.as_view(), name="shop"),
    path("urunler/<int:pk>/", ProductDetailView.as_view(), name="product-details"),
    path("iletisim/", ContactView, name="contact"),
]
