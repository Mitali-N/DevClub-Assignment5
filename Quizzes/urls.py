from django.urls import path
from . import views

urlpatterns  = [
    path('quiz', views.quizlist, name='quiz'),
    path('test/', views.quiz, name='test'),
    path('result', views.result, name='results'),
    path('createquiz/', views.makequiz, name='createquiz'),
    path('createquiz/addquestion', views.addques, name='addques'),
    path('quizcreated', views.quizcreated, name='quizcreated')
]