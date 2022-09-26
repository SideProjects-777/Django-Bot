from django.urls import path
from . import views

app_name = 'telegram'

urlpatterns = [
    path('send/', views.sendMessage, name="send"),
]