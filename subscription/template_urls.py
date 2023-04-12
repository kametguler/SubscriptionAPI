from django.urls import path
from subscription.views import ProductListView, ProductDetailView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("urunler/", ProductListView.as_view(), name="shop"),
    path("urunler/<int:pk>/", ProductDetailView.as_view(), name="product-details"),
]
