from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    
    def clean_username(self):
        data = self.cleaned_data["username"]
        user = User.objects.filter(username=data).exists()
        if user:
            raise ValidationError('This username is already exists')
        
        return data
    
    def clean_email(self):
        data = self.cleaned_data["email"]
        user = User.objects.filter(email=data).exists()
        if user:
            raise ValidationError('This email is already exists')
        
        return data
    
    def clean(self):
        cd = super().clean()
        password = cd.get('password')
        confirm_password = cd.get('confirm_password')
        
        if password and confirm_password and password!=confirm_password:
            raise ValidationError('Password must match')    
        

class UserLoginForm(forms.Form):
    
    username = forms.CharField(label='Username or Email', widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
        
        
        
        
    
    