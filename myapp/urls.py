
from django.urls import path 
# (include-> dite hobe)
from .views import * 

urlpatterns = [
    
    path("", home, name='home'),

    path('addstudent/', addstudent,  name='addstudent'),



]