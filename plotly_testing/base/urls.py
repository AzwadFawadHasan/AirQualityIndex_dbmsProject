from django.urls import path

from .views import TaskList, TaskDetail , TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', RegisterPage.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name= "login"),
    path('logout/', LogoutView.as_view(next_page = 'login'), name= "logout"),
    

    path('index/', views.index, name= "index"),
    path('index2/', views.index2, name= "index2"),
    path('index3/', views.index3, name= "index3"),
    path('index4/', views.index4, name= "index4"),
    
    path('boxplot/', views.boxplot, name= "boxplot"),
    path('dataDistribution/', views.dataDistribution, name= "dataDistribution"),
    path('boxplot2/', views.boxplot2, name= "boxplot2"),


    path('', TaskList.as_view(), name = "tasks"),
    path('task/<int:pk>/', TaskDetail.as_view(), name = "task"),
    path('task-create/', TaskCreate.as_view(), name = 'task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name = "task-update"),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name = "task-delete"),
]