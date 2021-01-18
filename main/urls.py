from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('settings', views.settings),
    path('login', views.login),
    path('question', views.question),
    path('ask', views.ask),
    path('tag', views.tag),
    path('registration', views.registration)
]
