from django.urls import path
from . import views

app_name = 'form'

urlpatterns = [
    path('load/', views.loadForm, name="load"),
    path('view/', views.viewResults, name="view"),
    path('save/', views.saveForm, name="save"),
    path('thanks/', views.thankYouPage, name="thankYou")
]
