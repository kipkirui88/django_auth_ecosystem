from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm

from django.shortcuts import redirect

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'role','phone_number', 'is_active', 'is_staff', 'is_superuser', 'password')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'role', 'phone_number')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'role', 'phone_number'),
        }),
    )

    def response_add(self, request, obj, post_url_continue=None):
        if "_addanother" in request.POST:
            return super().response_add(request, obj, post_url_continue)
        elif "_continue" in request.POST:
            return redirect(f'../{obj.pk}/')
        else:
            self.message_user(request, "User created successfully.")
            return redirect('..')  # Redirect to the list view


admin.site.register(User, UserAdmin)