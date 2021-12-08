from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import render
from django.utils.regex_helper import Choice
from django.views.generic import TemplateView, DetailView, ListView, View
from .models import *
from django.utils import timezone
from datetime import datetime
from django.db.models import Count


def index(request):
    if request.method == "POST" and request.is_ajax():
        # print(dict(request.POST.items()))
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        categories = request.POST.getlist('categories[]')
        schedule =  datetime.strptime(request.POST.get('schedule'), '%Y-%m-%dT%H:%M')
        task = Task.objects.create(title=title, description=description, priority=priority, schedule=schedule)
        for category in categories:
            category_obj = Category.objects.get(name=category)
            task.categories.add(category_obj)
        # print(task.categories.all())
        return JsonResponse({})
    return render(request, "todo/index.html", {"categories":Category.objects.all()})


def add_category(request):
    if request.method == "POST" and request.is_ajax():
        name = request.POST.get('name')
        description = request.POST.get('description')
        if Category.objects.filter(name__iexact=name.lower()).exists():
            return JsonResponse({'message':'This name already exists.'})
        else:    
            Category.objects.create(name=name, description=description)
        return JsonResponse({'message':'Your category was added successfully'})
    return render(request, "todo/add_category.html") 


def serializer_tasks(query):
    return JsonResponse({"object_list":list(query.values('pk', 'title', 'schedule'))})


def serializer_categories(query):
    return JsonResponse({"object_list":list(query.values('pk', 'name', 'description'))})

class TaskListView(ListView):
    model = Task
    def post(self, request, *args, **kwargs):
        print("inside class view")
        queryset = Task.objects.all().order_by('schedule')   
        return serializer_tasks(queryset)


def expired_tasks(request):
    print(request.method)
    print(request.is_ajax())
    if request.method == "POST" and request.is_ajax():
        queryset = Task.objects.filter(schedule__lt = timezone.now())   
        return serializer_tasks(queryset)
    return JsonResponse({})


def unexpired_tasks(request):
    if request.method == "POST" and request.is_ajax():
        queryset = Task.objects.filter(schedule__gte = timezone.now())   
        return serializer_tasks(queryset)
    return JsonResponse({})


def last_tasks(request):
    if request.method == "POST" and request.is_ajax():
        queryset = Task.objects.all().order_by('-time_created')[:3]  
        return serializer_tasks(queryset)
    return JsonResponse({})

class TaskDetailView(DetailView):
    model = Task

class CategoriesListView(ListView):
    model = Category


def empty_categories(request):
    if request.method == "POST" and request.is_ajax():
        queryset = Category.objects.all().annotate(Count('task')).filter(task__count=0)  
        return serializer_categories(queryset)
    return JsonResponse({})


def popular_categories(request):
    if request.method == "POST" and request.is_ajax():
        queryset = Category.objects.annotate(Count('task')).order_by('-task__count')[:3]  
        return serializer_categories(queryset)
    return JsonResponse({})

class CategoryDetailView(DetailView):
    model = Category
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.filter(categories=context["category"])
        return context
    
    






