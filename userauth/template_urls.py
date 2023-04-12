from django.urls import path
from .views import ProfileView, SubscriptionsView, OrdersView
from allauth.account.views import EmailView, LogoutView, PasswordResetView, LoginView, SignupView, PasswordChangeView

urlpatterns = [
    path('hesabim/', ProfileView.as_view(), name="profile"),
    # path('hesabim/email-degistir/', EmailView.as_view(template_name='profiles/change_email.html'),
    #      name='account_email'),
    path('hesabim/sifremi-degistir/', PasswordChangeView.as_view(template_name='profiles/change_password.html'),
         name='account_change_password'),
    path('cikis-yap/', LogoutView.as_view(template_name='profiles/logout.html'), name='account_logout'),
    path('hesabim/sifremi-sifirla/', PasswordResetView.as_view(template_name='profiles/reset_password.html'),
         name='account_reset_password'),
    path('giris-yap/', LoginView.as_view(template_name='profiles/login.html'), name='account_login'),
    path('kayit-ol/', SignupView.as_view(template_name='profiles/register.html'), name='account_signup'),
    path('aboneliklerim/', SubscriptionsView.as_view(), name='account_subscriptions'),
    path('siparislerim/', OrdersView.as_view(), name='account_orders'),
]
