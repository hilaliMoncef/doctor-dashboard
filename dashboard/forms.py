from django import forms

class ConnexionForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)