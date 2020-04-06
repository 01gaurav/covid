from django.shortcuts import render
from django import forms
from django.core import validators
from a1.forms import shpkprSU
def index(request):
    return render(request,'')

def newshpkpr(request):
    form=shpkprSU()
    if request.method=='POST':
        form=shpkprSU(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            raise forms.ValidationError("Error Form Is Invalid")    
    return render(request,'',{'form':form})  