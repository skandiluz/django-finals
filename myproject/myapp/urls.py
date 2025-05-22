from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact_view, name='contact'),
    path('student/add/', views.create_student, name='create_student'),
    path('students/', views.students_list, name='students_list'),

    path('students/', views.students_list, name='students_list'),
    path('student/add/', views.create_student, name='create_student'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('student/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    path('student/<int:student_id>/delete/', views.delete_student, name='delete_student'),

    path('student/create-direct/', views.create_student_direct, name='create_student_direct'),
    path('students/filter/', views.filter_students, name='filter_students'),
]