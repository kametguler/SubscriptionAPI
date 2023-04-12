from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminReadWritePermission(BasePermission):
    """
    Herkes okuyabilir, sadece adminler değişiklik yapabilir
    """

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            # Herkes okuyabilir
            return True
        else:
            # Sadece adminler değişiklik yapabilir
            return request.user and request.user.is_authenticated and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            # Herkes okuyabilir
            return True
        else:
            # Sadece adminler değişiklik yapabilir
            return request.user and request.user.is_authenticated and request.user.is_staff


class IsOwnerOrReadOnly(BasePermission):
    """
    Yalnızca kayıt sahibine yazma izni verir, diğer durumlarda sadece okuma izni verir.
    """

    def has_object_permission(self, request, view, obj):
        # Tüm kullanıcılara GET isteklerine izin verir.
        if request.method in SAFE_METHODS:
            return True

        # Kayıt sahibine PUT ve DELETE isteklerine izin verir.
        return obj.user == request.user
