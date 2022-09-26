from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('form/',include('form.urls')),
    path('bot/',include('telegram.urls')),
    path('about/', views.about),
    path('home/', views.home),
    path('admin/', admin.site.urls)
]

urlpatterns += staticfiles_urlpatterns()


#path('admin/', admin.site.urls),


