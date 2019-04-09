from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 30)
    password1 = forms.CharField(widget = forms.PasswordInput, max_length = 18)
    password2 = forms.CharField(widget = forms.PasswordInput, max_length = 18)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )

class TodoListform(forms.ModelForm):
    class Meta:
        model = models.TodoList
        fields = ["task", "Time","Accomplished"]
