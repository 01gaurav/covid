from django import forms
from a1.models import shpkprSU
from django.core import validators

def check_length(value):
    if(value.length()!=10):
        raise forms.ValidationError("Invalid Mobile No")

class newshpkpr(forms.ModelForm):
    first_name=forms.CharField()
    last_name=forms.CharField() 
    email=forms.EmailField()
    location=forms.CharField()
    mobile_no=forms.IntegerField(validators=[check_length])
    bootcatcher=forms.CharField(required=False,
                            widget=forms.HiddenInput,
                            validators=[validators.MaxLengthValidator(0)] )
    class Meta():
        model=shpkprSU
        fields='__all__'