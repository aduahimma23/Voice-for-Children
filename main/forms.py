from typing import Any
from django import forms
from .models import Donation, ReportAbuse, Contact, UserRegistration

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'

class ChildAbuseReporterForm(forms.ModelForm):
    class Meta:
        model = ReportAbuse
        exclude = ['add_new_region', 'add_new_abuse_type']

        def clean(self):
            clean_data = super.clean()
            


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'content']

        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


    def clean(self) -> dict[str, Any]:
        clean_data = super().clean()
        name = clean_data.get('name')
        email = clean_data.get('email')
        phone = clean_data.get('phone_number')
        content = clean_data.get('content')

        if not name and not email and not phone and not content:
            raise forms.ValidationError('Please fill in all fields.')
        
        return clean_data
    
class UserCreateForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = '__all__'