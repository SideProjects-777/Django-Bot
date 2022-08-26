from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.loadForm),
    path('view/', views.viewResults),
    path('dummy/', views.dummy)
]
