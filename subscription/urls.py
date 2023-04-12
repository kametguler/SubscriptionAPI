from django.urls import path
from subscription.views import UserSubscriptionDetail, UserSubscriptionList, ProductList, ProductDetail, ProductListView

urlpatterns = [
    # api view
    path("aboneliklerim/", UserSubscriptionList.as_view(), name="subscriptions"),
    path("aboneliklerim/<int:product_id>/", UserSubscriptionDetail.as_view(), name="subscription-details"),
    path("urunler/", ProductList.as_view(), name="subscriptions"),
    path("urunler/<int:pk>/", ProductDetail.as_view(), name="subscription-details"),
]
