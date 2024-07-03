from django import forms
from.models import contact_us
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class ContactForm(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    class Meta:
        model = User
        fields =  ( 'username','password',)

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    phone2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    