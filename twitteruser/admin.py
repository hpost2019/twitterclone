from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import TwitterUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = TwitterUser
    list_display = ['username', 'email', ]
    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('followed', )}),
    )


admin.site.register(TwitterUser, CustomUserAdmin)
