from django import forms
from django.contrib.auth.forms import UserCreationForm
from letters.models import User

class UserForm(UserCreationForm):
    lettercase_url = forms.CharField(required=False)
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "lettercase_url"]
