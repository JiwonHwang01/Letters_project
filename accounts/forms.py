from django import forms
from django.contrib.auth.forms import UserCreationForm
from letters.models import User
import uuid
import base64
import codecs

def generate_random_slug_code(length=12):
    
    return base64.urlsafe_b64encode(
        codecs.encode(uuid.uuid4().bytes, "base64").rstrip()
    ).decode()[:length]

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    # lettercase_url = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
