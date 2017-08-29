from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    mobile = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'mobile', 'password1', 'password2', )
