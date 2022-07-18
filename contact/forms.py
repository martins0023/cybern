from django import forms
from django.contrib.auth.models import User
from .models import Message

class contact_us_name(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['full_name']
        
class contact_us_email(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['email_address']
    
class contact_us_subject(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject']
        
class contact_us_message(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']