'''
Created on Jul 7, 2012

@author: sudharshan
'''
from django import forms
from taggit.forms import * 
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=6)
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField()
    
class UpdateProfile(forms.Form):
    Visited=forms.CharField(max_length=30)
    ToVisit=forms.CharField(max_length=30)
    Feedback=forms.CharField(widget=forms.Textarea)
    
class SellForm(forms.Form):
    title=forms.CharField(max_length=50)
    city=forms.CharField(max_length=50)
    category=forms.CharField(max_length=50)
    image=forms.ImageField()
    expirydate=forms.DateField()
    price=forms.CharField(max_length=50)
    tags=TagField()
    
    
