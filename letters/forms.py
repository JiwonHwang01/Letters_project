from django import forms
from .models import Letter

class LetterForm(forms.ModelForm):
    
    class Meta:
        model = Letter
        fields = ['visitor_id', 'title', 'letter_text']