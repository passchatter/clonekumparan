from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class loginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'your username',
        'class':'w-full py-4 px-6 rounded-xl border border-slate-300'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'your password',
        'class':'w-full py-4 px-6 rounded-xl border border-slate-300'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'your username',
        'class':'w-full py-4 px-6 rounded-xl border border-slate-300'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'your email',
        'class':'w-full py-4 px-6 rounded-xl border border-slate-300'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'create password',
        'class':'w-full py-4 px-6 rounded-xl border border-slate-300'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'confirmation',
        'class':'w-full py-4 px-6 rounded-xl border border-slate-300'
    }))