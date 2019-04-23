from django.contrib import admin

from django.contrib.auth import admin as auth

from .models import UUIDUser


# UserAdmin
# - - - - - - - - - - - - - - - - - - -
class UserAdmin(auth.UserAdmin):

    fieldsets = (
        ('Personal info', {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'cpf', 'registration')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ('groups', 'user_permissions')


# Register
# - - - - - - - - - - - - - - - - - - -
admin.site.register(UUIDUser, UserAdmin)