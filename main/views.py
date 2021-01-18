from django.shortcuts import render
# Create your views here.

questions = [
    {
        'id': idx,
        'title': f'title{idx}',
        'text': 'text text',
    } for idx in range(5)
]

def index(request):
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
