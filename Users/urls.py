from django.urls import path
from . import views
from .models import Courses


urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('home/', views.home, name="home"),
    path('coursepage/',views.course_page, name="coursepage"),
    path('course_grades/',views.marks, name="coursegrades"),
    path('gradesheet/',views.gradesheet, name="gradesheet"),
    path('uploadmarks/',views.uploadmarks, name="uploadmarks"),
    path('uploadfinal/',views.uploadfinal, name="uploadfinal"),
    #path('trial/',views.trial, name="trial")
]