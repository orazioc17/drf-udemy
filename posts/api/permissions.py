from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    """
    Clase con la que hacemos algo parecido a IsAuthenticatedOrReadOnly, pero en vez de que sea para cualquier usuario
    autenticado, es solo para los staff, es decir, solo los staff pueden usar metodos tipo PUT, POST, DELETE y demas
    """
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff
