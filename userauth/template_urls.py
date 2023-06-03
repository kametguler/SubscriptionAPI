from django.urls import path, include, re_path
from .views import ProfileView, SubscriptionsView, OrdersView
from allauth.account.views import EmailView, LogoutView, PasswordResetView, LoginView, SignupView, PasswordChangeView, \
    PasswordResetDoneView, PasswordResetFromKeyView, PasswordResetFromKeyDoneView

urlpatterns = [
    # path("accounts/", include("allauth.account.urls")),
    re_path("hesabim/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
            PasswordResetFromKeyView.as_view(template_name="profiles/account_reset_password_from_key.html"),
            name="account_reset_password_from_key"),
    path(
        "password/reset/key/done/",
        PasswordResetFromKeyDoneView.as_view(template_name="profiles/account_reset_password_from_key_done.html"),
        name="account_reset_password_from_key_done"
    ),
    path('hesabim/', ProfileView.as_view(), name="profile"),
    # path('hesabim/email-degistir/', EmailView.as_view(template_name='profiles/change_email.html'),
    #      name='account_email'),
    path('hesabim/sifremi-degistir/', PasswordChangeView.as_view(template_name='profiles/change_password.html'),
         name='account_change_password'),
    path('cikis-yap/', LogoutView.as_view(template_name='profiles/logout.html'), name='account_logout'),
    path('hesabim/sifremi-sifirla/', PasswordResetView.as_view(template_name='profiles/reset_password.html'),
         name='account_reset_password'),
    path('hesabim/sifremi-sifirlandi/',
         PasswordResetDoneView.as_view(template_name='profiles/reset_password_done.html'),
         name='account_reset_password_done'),
    path('giris-yap/', LoginView.as_view(template_name='profiles/login.html'), name='account_login'),
    path('kayit-ol/', SignupView.as_view(template_name='profiles/register.html'), name='account_signup'),
    path('aboneliklerim/', SubscriptionsView.as_view(), name='account_subscriptions'),
    path('siparislerim/', OrdersView.as_view(), name='account_orders'),
]
