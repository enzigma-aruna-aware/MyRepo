"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class ContactForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    FirstName=forms.CharField(label="First Name",max_length=80,required=False,
                                    widget=forms.TextInput({
                                        'class': 'form-control',
                                        'placeholder': 'FirstName'}))

    LastName=forms.CharField(label="Last Name",max_length=80,
                                    widget=forms.TextInput({
                                        'class': 'form-control',
                                        'placeholder': 'LastName'}))
    Email=forms.EmailField(label="Email",max_length=80,required=True,
                                    widget=forms.EmailInput({
                                        'class': 'form-control',
                                        'placeholder': 'Email'}))
    Mobile=forms.DecimalField(label="Mobile",max_digits=10,
                                    widget=forms.NumberInput({
                                        'class': 'form-control',
                                        'placeholder': 'Mobile'}))
