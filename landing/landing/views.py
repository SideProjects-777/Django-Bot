from django.http import HttpResponse;
from django.shortcuts import render


def firstPage(request):
    a = '<h1>Hello World</h1>'
    txt = 'New Text'
    return render(request, 'index.html',{
        'a':a,
        'text':txt
    })