from django.db import models
from django.utils.timezone import now
from datetime import date
from django.contrib.auth.models import User

# TaskList model inside which there will be tasks
class TaskList(models.Model):
    name = models.CharField(max_length = 50)
    created_at = models.DateField(default = date.today)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name}--{self.created_at}"

class Tasks(models.Model):
    choice = {"high": "High", "medium": "Medium", "low": "Low"}
    name = models.CharField(max_length = 20, default = 'HomeWork')
    description = models.TextField(blank = True, null = True)
    created_at = models.DateField(default = date.today)
    due_date = models.DateField(blank = True, null = True)
    priority = models.CharField(max_length = 20, choices = choice, default = "High")
    task_list = models.ForeignKey(TaskList, on_delete = models.CASCADE, default = 1)
    isDone = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.name}--|{self.task_list}|--{self.created_at}"
