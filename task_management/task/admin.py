from django.contrib import admin
from task.models import TaskModel

# Register your models here.
class TaskModelAdmin(admin.ModelAdmin):
    list_display=['taskTittle','taskDescription']
admin.site.register(TaskModel,TaskModelAdmin)
