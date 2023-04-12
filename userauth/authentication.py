from rest_framework.authentication import TokenAuthentication, get_authorization_header
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_jwt.authentication import jwt_get_username_from_payload


class JWTAuthentication(TokenAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        auth_header = get_authorization_header(request).split()
        if not auth_header:
            return None
        if len(auth_header) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise AuthenticationFailed(msg)
        elif len(auth_header) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise AuthenticationFailed(msg)

        try:
            token = auth_header[1].decode('utf-8')
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        from rest_framework_jwt.authentication import jwt_decode_handler
        try:
            payload = jwt_decode_handler(token)
        except:
            msg = _('Invalid authentication. Could not decode token.')
            raise AuthenticationFailed(msg)

        user = self.authenticate_user(payload)

        return (user, token)

    def authenticate_user(self, payload):
        from django.contrib.auth import get_user_model
        User = get_user_model()

        try:
            username = jwt_get_username_from_payload(payload)
            user = User.objects.get(**{User.USERNAME_FIELD: username})
        except User.DoesNotExist:
            msg = _('Invalid signature')
            raise AuthenticationFailed(msg)

        if not user.is_active:
            msg = _('User account is disabled.')
            raise AuthenticationFailed(msg)
