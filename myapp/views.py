from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    students = student.object.all()
    return render(request, 'index.html', {"name":students })

def addStudent(request):
    name = request.POST.get('name')
    roll = request.POST.get('roll')
    semester = request.POST.get('semester')
    department = request.POST.get('department')
    cgpa = request.POST.get('cgpa')
    return render(request, 'addstudent.html')