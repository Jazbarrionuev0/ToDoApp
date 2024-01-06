from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, EscribeTuPensamiento

# Create your views here.
def blog(request):
        return render(request, 'blog.html', {
            'form': EscribeTuPensamiento()
        })

def createTask(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            titulo=request.POST['titulo'], decripcion=request.POST['descripcion'], project_id=1)
        return redirect('/tasks/')


def index(request):
    title = 'Pagina de inicio'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    title = 'Este es el about'
    return render(request, 'about.html', {
        'title': title
    })


def projects(request):
    proyectos = Project.objects.all()
    return render(request, 'projects.html', {
        'proyectos': proyectos
    })


def tasks(request):
    tareas = Task.objects.all()
    return render(request, 'tasks.html', {
        'tareas': tareas
    })

