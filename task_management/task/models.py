from django.db import models

# Create your models here.
class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True)
    taskTittle = models.CharField(max_length=15)
    taskDescription = models.CharField(max_length=30)
    is_Completed = models.BooleanField(default=False)
    
