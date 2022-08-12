from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TaskForm # importar o fomrulário

from .models import Task

def taskList(request):
    tasks = Task.objects.all().order_by('-created_at') #ordenar do mais novo para o mais antigo.
    return render(request, 'tasks/list.html', {'tasks':tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST) 
        
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm() # definir uma variável chamando ela para o front end.
        return render(request, 'tasks/addtask.html', {'form': form})

def editTask(request, id):
    task = get_object_or_404(Task, pk=id) # model referência
    form = TaskForm(instance=task) #puxar o formulário e mostrar para o usuário.
    
    if(request.method == "POST"):
        form = TaskForm(request.POST, instance=task) 

        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': {task}})

    else: 
        return render(request, 'tasks/edittask.html', {'form': form, 'task': {task}}) #exibição da view no template com os dados pré acoplados.

def helloWorld(request):
    return HttpResponse('Hello World!')

def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name':name})



