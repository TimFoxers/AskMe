from django.shortcuts import render
from main.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)

def index(request):
    questions = Article.objects.all()
    page = paginate(questions, request, 2)
    return render(request, 'index.html', {
        'page': page,
        'page_end_diff': page.paginator.num_pages - page.number,
        'user': request.user,
    })

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
