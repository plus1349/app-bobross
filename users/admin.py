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
    inlines = (UserPaintingLayerAdmin,)
    list_display = ('id', 'user', 'painting')
    list_display_links = ('user', 'painting')
    list_filter = ('user',)
    search_fields = ('user', 'painting')


@register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2')
        }),
    )
    add_form = UserCreateForm
    change_password_form = AdminPasswordChangeForm
    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal info'), {'fields': ('name', 'email', 'phone')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('date_joined', 'last_login')}),
    )
    form = UserUpdateForm
    inlines = (TokenAdmin,)
    list_display = ('id', 'name', 'email', 'is_superuser', 'auth_token')
    list_display_links = ('name', 'email')
    list_filter = ('is_staff', 'is_superuser')
    readonly_fields = ('date_joined', 'last_login')
    search_fields = ('name', 'email')
    ordering = ()
