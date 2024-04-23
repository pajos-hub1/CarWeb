from django import forms

class UsernameForm(forms.Form):
    username = forms.CharField(label='Username or Phone Number')

class PasswordForm(forms.Form):
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)

