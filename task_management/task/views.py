from django.shortcuts import render,redirect
from task.forms import TaskForm
from task.models import TaskModel

# Create your views here.
def home(request):
    return render(request,'base.html')

def add_task(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            print(task.cleaned_data)
            return redirect('show_task_page')
            
    else:
        task = TaskForm()
    
    return render(request,'add_task.html',{'form':task})




def show_task(request):
    task=TaskModel.objects.all()
    return render(request,'show_task.html',{'data':task})


def edit_task(request,id):
    task = TaskModel.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task_page')
    return render(request,'add_task.html',{'form':task_form})

def delete_task(request,id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect('show_task_page')


def complete_task(request,id):
    task = TaskModel.objects.get(pk=id)
    task.is_Completed=True
    task.save()
    return redirect('show_task_page')
    
  

def show_complete_task(request):
    return render(request,"complete_task.html")
    