from django.shortcuts import render
from main.models import Article
# Create your views here.

def index(request):
    questions = Article.objects.all()
    return render(request, 'index.html', {'questions': questions})

def settings(request):
    return render(request, 'settings.html')

def login(request):
    return render(request, 'login.html')

def question(request):
    return render(request, 'question.html')

def ask(request):
    return render(request, 'ask.html')

def tag(request):
    return render(request, 'tag.html')

def registration(request):
    return render(request, 'registration.html')
