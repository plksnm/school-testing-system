from django.contrib import admin
from .models import Tasks
from django.contrib.auth.admin import UserAdmin

class TasksAdmin(admin.ModelAdmin):
 	list_display = ('name','task_path_input','task_path_output')

admin.site.register(Tasks, TasksAdmin)
