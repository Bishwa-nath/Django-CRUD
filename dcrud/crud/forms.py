from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . models import Record

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>User name is required</small></span>'
        
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Password is required</small></span>'

        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password</small></span>'


class RecordForm(forms.ModelForm):
    first_name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    phone = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}))
    email = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    street = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Street', 'class': 'form-control'}))
    city = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}))
    state = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}))
    zip_code = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Zip code', 'class': 'form-control'}))

    class Meta:
        model = Record
        exclude = ("user", )