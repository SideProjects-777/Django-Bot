from django.shortcuts import render
from .models import Form

from . import forms


def loadForm(request):
    form = forms.CreateForm() 
    return render(request, 'form/loadForm.html',{'form':form} )

def viewResults(request):
    results = Form.objects.all().order_by('currDay')
    return render(request, 'form/viewResults.html', {'results':results} )

def deleteRow(request):
    results = Form.objects.all().order_by('currDay')
    return render(request, 'form/viewResults.html', {'results':results} )

def editRow(request):
    results = Form.objects.all().order_by('currDay')
    return render(request, 'form/viewResults.html', {'results':results} )
