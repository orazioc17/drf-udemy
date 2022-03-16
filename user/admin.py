from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Personalizando la vista de usuario en el admin de django, seleccionando que campos mostrar y en que orden y
    agrupacion
    """
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informacion Personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Redes Sociales', {'fields': ('web_site', 'twitter')}),
    )
