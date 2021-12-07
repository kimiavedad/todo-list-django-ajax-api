from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, View
from .models import *
from datetime import datetime

class TaskDetailView(DetailView):
    model = Task

class TaskListView(ListView):
    model = Task

    def post(self, request, *args, **kwargs):
        list_sorted_tasks = Task.objects.order_by('schedule')   
        context = {
            "object_list": list_sorted_tasks
        } 
        return render(request, "todo/task_list.html", context)

def index(request):
    if request.method == "POST" and request.is_ajax():
        print("y josn bargasht")
        return JsonResponse({})
    return render(request, "todo/index.html")

# class IndexView(TemplateView):
#     template_name = "todo/index.html"
#     def post(self, request, *args, **kwargs):
#         # print(dict(request.POST.items()))
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         priority = request.POST.get('priority')
#         category = request.POST.get('category').lower()
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         schedule =  datetime.strptime(date + " " + time, '%Y-%m-%d %H:%M')
#         try:
#             category_in_db = Category.objects.get(name=category)
#         except Category.DoesNotExist:
#             category_in_db = Category(name=category)
#             category_in_db.save()
    
#         # print(category_in_db)
#         task = Task(title=title, description=description, priority=priority, category=category_in_db, schedule=schedule)
#         task.save()
#         return render(request, self.template_name)


class CategoriesListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.filter(category=context["category"])
        # print(dict(context.items()))
        return context
    
    






