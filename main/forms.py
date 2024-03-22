from typing import Any
from django import forms
from .models import Donation, ChildAbuseReporter, Contact, UserRegistration

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'

class ChildAbuseReporterForm(forms.ModelForm):
    class Meta:
        model = ChildAbuseReporter
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'content']

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