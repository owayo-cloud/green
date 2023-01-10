from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    """Form for user input registration

    Args:
            UserCreationForm (form): django inbuilt user creation form
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control'}),
        }
