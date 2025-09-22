from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test),
    path('tasks/', views.getTasks),
    path('tasks/create',views.create_task),
    path("tasks/delete/<int:pk>",views.delete_task)
]
