from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from .forms import NumbInPage
from .models import News


class ClassHome(TemplateView):
    template_name = 'testapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Urban module_19 "Пагинация"'
        return context

def index1(request):
    context = {}
    post = News.objects.all().order_by('-created_at')
    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    context['title'] = 'Urban module_19 "Пагинация" пункт 1'
    return render(request, 'testapp/index1.html', context=context)

def index2(request):

    context = {}
    posts_in_page= 2
    if request.method == 'POST':
        form = NumbInPage(request.POST)
        context['form'] = form
        if form.is_valid():
           posts_in_page = request.POST.get('posts_in_page')
    else: # request.method == 'GET':
        form = NumbInPage(request.GET)
        context['form'] = form
        if form.is_valid():
            posts_in_page = request.GET.get('posts_in_page')

    posts = News.objects.all().order_by('-created_at')
    paginator = Paginator(posts, posts_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = NumbInPage()
    context['page_obj'] = page_obj
    context['title'] = 'Urban module_19 "Пагинация" пункт 2'
    context['posts_in_page'] = posts_in_page
    context['form'] = form
    context['range_posts'] = range(1, len(posts)+1)

    return render(request, 'testapp/index2.html', context=context)
