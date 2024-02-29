from django.urls import path
from . import views

urlpatterns = [
    path('tasklists/', views.index, name = "index"),
    path('addnewtasklist/', views.create_tasklist, name = "addtasklist"),
    path('addnewtask/<int:id>', views.create_task_in_tasklist, name = "addtasks"),
    path('showtasks/<int:id>/<str:listname>/', views.showTasks, name = "mytasks"),
    path('checkboxonoff/', views.check_uncheck_checkbox, name = "check_uncheck"),
    path("updatetask/<int:id>", views.update_task, name = "updatetask"),
    path("deletetask/<int:id>", views.delete_task, name = "deletetask"),
    path("deletelist/<int:id>", views.delete_list, name = "deletelist")
]
