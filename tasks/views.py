from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'tasks':tasks , 'form' : form}
    template_name = 'tasks/index.html'
    return render(request,template_name,context)

def update(request,id):
    task = Task.objects.get(id = id)
    form = TaskForm(instance=task)
    context = {'form':form}
    template = 'tasks/update.html'

    if request.method == 'POST':
        form= TaskForm(request.POST,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')

    return(render(request,template,context))

def delete(request,id):
    task = Task.objects.get(id = id)
    context = {'task':task}
    template_name = 'tasks/delete.html'
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request,template_name,context)
