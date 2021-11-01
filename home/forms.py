from django import forms
from .models import ContactUsMessage

class ContactUsForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = ContactUsMessage
        fields = ('name', 'email', 'subject', 'message')
