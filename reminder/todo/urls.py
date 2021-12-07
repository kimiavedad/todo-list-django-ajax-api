from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]