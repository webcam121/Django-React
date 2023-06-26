from django import forms
from django.core.validators import RegexValidator


class AddPatientForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=32,
        label='First Name'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=32,
        label='Last Name'
    )
    # phone_number = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control'}),
    #     max_length=254,
    #     label='Phone Number'
    # )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(
        validators=[phone_regex], 
        max_length=17
    )