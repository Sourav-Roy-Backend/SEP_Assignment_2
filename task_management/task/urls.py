from django.urls import path
from task.views import home,add_task,show_task,edit_task,delete_task,complete_task,show_complete_task

urlpatterns = [
    path('',home, name='homepage'),
    path('add_task/',add_task, name='add_task_page'),
    path('show_task/',show_task, name='show_task_page'),
    path('edit_task/<int:id>',edit_task, name='edit_task_page'),
    path('delete_task/<int:id>',delete_task, name='delete_task_page'),
    path('complete_task/<int:id>',complete_task, name='complete_task_page'),
    path('show_complete_task/',show_complete_task, name='show_complete_task_page'),
    
    
    
]
