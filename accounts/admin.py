from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ActNowUserChangeForm, ActNowUserCreationForm
from .models import ActNowUser


class ActNowUserAdmin(UserAdmin):
    add_form = ActNowUserCreationForm
    form = ActNowUserChangeForm
    model = ActNowUser
    list_display = (
        "email",
        "username",
        "is_staff",
        "is_superuser",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "username", "password", "groups")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(ActNowUser, ActNowUserAdmin)
