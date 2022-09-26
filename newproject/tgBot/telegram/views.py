from cgitb import text
from django.http import HttpResponse
from django.shortcuts import render
from telegram.sendMessage import sendTelegram

def sendMessage(request):
    print(request.GET.get('message'))
    textMessage =request.GET.get('message')
    sendTelegram(textMessage)
    return HttpResponse(textMessage)
