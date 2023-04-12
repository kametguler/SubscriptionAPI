SECRET_KEY = 'django-insecure-y$-c2v&ja+ipi8ksfzfb-w22w$ersh@^az!1gs7(*d3m_a-+ho'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "test_db",
        'USER': 'postgres',
        'PASSWORD': "kamet789kamet"
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
