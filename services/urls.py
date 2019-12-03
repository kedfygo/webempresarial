from django.urls import path
from . import views


urlpatterns = [
    #Paths de Services
    path('', views.services, name='services'),    
]


