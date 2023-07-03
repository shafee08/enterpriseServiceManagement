from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Service
from django.forms import Textarea

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("first_name","last_name", "email", "password1", "password2")
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
           
        for field in self.fields:
            self.fields[field].help_text = "<span class='help-text'>%s</span>" % self.fields[field].help_text


class RentForm(forms.Form):
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','min':1}))


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title','category', 'price', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control','min':0}),
            'description': forms.Textarea(attrs={'class': 'form-control','rows':5}),
        }



