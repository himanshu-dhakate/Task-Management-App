from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('addnewtasklist/', views.create_tasklist, name = "addtasklist"),
    path('addnewtask/<int:id>', views.create_task_in_tasklist, name = "addtasks"),
    path('showtasks/<int:id>', views.showTasks, name = "mytasks"),
    path('checkboxonoff/', views.check_uncheck_checkbox, name = "check_uncheck")
]
