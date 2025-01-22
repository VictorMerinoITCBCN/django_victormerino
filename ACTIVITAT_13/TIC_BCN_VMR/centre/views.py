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
    student = Student.objects.get(id=id)
    context = {
        "user": student,
        "modules": student.modules.all()
    }
    return render(request, "student.html", context)

def get_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    context = {
        "user": teacher,
        "modules": teacher.modules.all()
    }
    return render(request, "teacher.html", context)