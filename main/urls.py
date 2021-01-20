from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    path('settings', views.settings),
    path('login', views.login),
    path('question/<int:question_id>/', views.question, name='question'),
    path('ask', views.ask),
    path('tag', views.tag),
    path('registration', views.registration)
]
