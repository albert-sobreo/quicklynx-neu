from django.urls import path, include
from app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.login, name='login'),
    path('makelogins/', views.makelogins, name='makelogins'),
    path('home/', views.home, name='home'),
    path('help/', views.help, name='help'),
    path('registerstudent/', views.registerstudent, name='registerstudent'),
    path('register-as-student/', views.register_as_student, name='register-as-student'),
    path('verification/', views.verification, name='verification'),
    path('makeverifications/', views.makeverifications, name='makeverifications'),
    path('logout/', views.logoutview, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register-as-professor/', views.register_as_professor, name='register-as-professor'),
    path('registerprofessor/', views.registerprofessor, name='registerprofessor'),
    path('classroom/<str:room_name>', views.classroom, name='classroom'),
    path('makepost/<str:room_name>', views.makepost, name='makepost'),
    path('makepostfromhome/', views.makepostfromhome, name='makepostfromhome'),
    path('makeclassroom/', views.makeclassroom, name='makeclassroom'),
    path('joinclassroom/', views.joinclassroom, name='joinclassroom')
]