from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Tasks)
admin.site.register(models.TaskList)
