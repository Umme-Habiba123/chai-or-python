from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import *

# Create your views here.

def home(request):
    students = Student.object.all()
    return render(request, 'index.html', {"name":students })

# def addStudent(request):
#     name = request.POST.get('name')
#     roll = request.POST.get('roll')
#     semester = request.POST.get('semester')
#     department = request.POST.get('department')
#     cgpa = request.POST.get('cgpa')


def addstudent(request):
    if request.method =='POST':
        form = StudentForm(request.POST)

        if form.is_valid():
         form.save()
        return redirect('home')   

    else:
        form =StudentForm()

    return render(request, 'addstudent.html',{
        'form': form 
    })

