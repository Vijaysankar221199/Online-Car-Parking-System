from django import forms
from django.core import validators
from myapp.models import User
from .models import *

class Authentic(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields =("username","password","first_name","last_name")




class UploadForm(forms.ModelForm):

    class Meta:
        model = scanupload
        fields = ['slot_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('car_number','Phonenumber')


class otp(forms.ModelForm):

    class Meta:
        model = otp
        fields = ['name','phone', 'otp','visiname']
