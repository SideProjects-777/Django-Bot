import site
from django.shortcuts import render
from .models import Form
from django.shortcuts import redirect

from . import forms


def loadForm(request):
    form = forms.CreateForm() 
    return render(request, 'form/loadForm.html',{'form':form} )

def viewResults(request):
    results = Form.objects.all().order_by('work_date')
    return render(request, 'form/viewResults.html', {'results':results} )

def saveForm(request):
    print(request.POST)
    crew_status =request.POST.get('crewstatus')
    site_ID = request.POST.get('siteid')
    CX_status = request.POST.get('cxstatus')
    completeness =request.POST.get('completeness')
    daily_progress = request.POST.get('daily')
    next_day_plan =request.POST.get('nextDay')
    notes = request.POST.get('notes')
    market =request.POST.get('market')
    user = request.POST.get('fullname')
    data = Form(user=user,market=market,notes=notes,next_day_plan=next_day_plan,daily_progress=daily_progress,completeness=completeness,CX_status=CX_status,site_ID=site_ID, crew_status=crew_status)
    data.save()
    response = redirect('/form/thanks/')
    return response


def thankYouPage(request):
    return render(request, 'form/thankYou.html' )