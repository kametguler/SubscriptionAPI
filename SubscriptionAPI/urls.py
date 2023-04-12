from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('subscription.urls')),
    path('api/auth/', include('userauth.urls')),
    path('', include('subscription.template_urls')),
    path('', include('shopping.urls')),
    path('', include('userauth.template_urls')),
]
