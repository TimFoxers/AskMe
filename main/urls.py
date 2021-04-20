from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('login', views.login, name='login'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('ask', views.ask, name='ask'),
    path('tag', views.tag, name='tag'),
    path('registration', views.registration, name='registration')
]
