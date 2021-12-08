from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),

    path('tasks/', TaskListView.as_view(), name='tasks'),

    path('expired_tasks/', expired_tasks, name="expired_tasks"),

    path('unexpired_tasks/', unexpired_tasks, name="unexpired_tasks"),

    path('last_tasks/', last_tasks, name="last_tasks"),

    path('categories/', CategoriesListView.as_view(), name='categories'),

    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),

    path('empty_categories/', empty_categories, name='empty_categories'),

    path('popular_categories/', popular_categories, name='popular_categories'),

    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]