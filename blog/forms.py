from django import forms
from django.contrib.auth.models import User


class contact_us(forms.ModelForm):
    full_name = forms.CharField()
    email_address = forms.CharField()
    subject = forms.CharField()
    message = forms.CharField()

    class Meta:
        model = User
        fields = ['full_name', 'email_address', 'subject', 'message']