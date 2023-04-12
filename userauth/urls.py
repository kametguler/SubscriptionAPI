from django.urls import path, include
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    # path('api-token-auth/', obtain_jwt_token, name='api_token_auth'),  # JWT token alma
    # path('api-token-refresh/', refresh_jwt_token, name='api_token_refresh'),  # JWT token yenileme
    # path('api-token-verify/', verify_jwt_token, name='api_token_verify'),  # JWT token doğrulama
    path('', include('rest_auth.urls')),  # Allauth urls
    path('registration/', include('rest_auth.registration.urls')),  # Allauth Registration urls
]
