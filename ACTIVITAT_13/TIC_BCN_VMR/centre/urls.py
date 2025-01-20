from django.urls import path
from . import views

urlpatterns = [
    path('students', views.student_index),
    path('teachers', views.teacher_index),
    path('student/<int:id>/', views.get_student),
    path('teacher/<int:id>/', views.get_teacher)
]
