from django.contrib.admin import register, site, ModelAdmin, TabularInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.models import Token

from users.forms import UserCreateForm, UserUpdateForm
from users.models import User, UserPainting, UserPaintingLayer


site.unregister(Group)
site.unregister(Token)


class TokenAdmin(TabularInline):
    model = Token
    extra = 0
    classes = ('collapse',)


class UserPaintingLayerAdmin(TabularInline):
    model = UserPaintingLayer
    extra = 0
    classes = ('collapse',)


@register(UserPainting)
class UserPaintingAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('finish',)}),
        (_('Relations'), {'fields': ('user', 'painting')}),
        (_('Files'), {'fields': ('progress',)})
    )
    list_display = ('id', 'user', 'painting')
    list_display_links = ('user', 'painting')
    list_filter = ('painting', 'user', 'painting__free', 'painting__layers_count', 'painting__size_name')
    ordering = ('painting__position', 'painting__title', 'painting__id', 'id')
    search_fields = ('painting__title',)


@register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {'fields': ('password1', 'password2')}),
    )
    add_form = UserCreateForm
    change_password_form = AdminPasswordChangeForm
    date_hierarchy = 'date_joined'
    fieldsets = (
        (None, {'fields': ('password', 'auth_token')}),
        (_('Personal info'), {'fields': ('email', 'device_id', 'name', 'phone')}),
        (_('Files'), {'fields': ('state',)}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('date_joined', 'last_login')}),
    )
    form = UserUpdateForm
    list_display = ('id', 'email', 'device_id', 'auth_token')
    list_display_links = ('email', 'device_id')
    list_filter = ('is_staff', 'is_superuser')
    readonly_fields = ('date_joined', 'last_login', 'auth_token')
    search_fields = ('name', 'email')
    ordering = ('-is_superuser', '-is_staff', 'id', 'email', 'name')
