from django.shortcuts import render
from .models import Student, Teacher

def student_index(request):
    context = {
        "role": "Alumnes",
        "info_url": "http://127.0.0.1:8000/student/",
        "users": Student.objects.all()
    }
    return render(request, "user.html", context)

def teacher_index(request):
    context = {
        "role": "Profesors", 
        "info_url": "http://127.0.0.1:8000/teacher/",
        "users": Teacher.objects.all()
    }
    return render(request, "user.html", context)

def get_student(request, id):
    context = {
        "user": Student.objects.get(id=id)
    }
    return render(request, "student.html", context)

def get_teacher(request, id):
    context = {
        "user": Teacher.objects.get(id=id)
    }
    return render(request, "teacher.html", context)