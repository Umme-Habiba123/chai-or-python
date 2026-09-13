
# from django.contrib import admin -> (lagbe na)
from django.urls import path, include 
# (include-> dite hobe)
from .views import * 
# (myapp ->lagbe na)
urlpatterns = [
    # path('admin/', admin.site.urls), (lagbe na)
    path("",include('myapp.urls'))


]
