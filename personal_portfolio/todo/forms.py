# from django.forms import EmailField
#
# from django.utils.translation import ugettext_lazy as _
#
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
#
#
# class UserCreationForm(UserCreationForm):
#     email = EmailField(label=_("Email address"), required=True,
#         help_text=_("Required."))
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")
#
#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user

# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django import forms
# from django.contrib.auth.models import User


# class CustomAuthFormUser(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

# class CustomAuthenticationForm(AuthenticationForm):
#     email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Todo


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']
