from django import forms
from .models import User

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role', 'phone_number')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.is_active = True  # Ensure the user is active by default
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role', 'phone_number')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user