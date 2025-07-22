from django import forms
from django.contrib.auth.forms import UserCreationForm
from letters.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    lettercase_url = forms.CharField(required=False)
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email","lettercase_url"]
