from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .forms import UserCreateForm, UserUpdateForm
from .models import User


class UserAdmin(BaseUserAdmin):
    exclude = ('first_name', 'last_name', 'date_joined', 'last_login', 'groups', 'user_permissions')
    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal info'), {'fields': ('name', 'email', 'phone')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2')}
        ),
    )
    add_form = UserCreateForm
    change_password_form = AdminPasswordChangeForm
    form = UserUpdateForm
    list_display = ('id', 'name', 'email', 'is_superuser')
    list_display_links = ('name', 'email')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('name', 'email')
    ordering = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
