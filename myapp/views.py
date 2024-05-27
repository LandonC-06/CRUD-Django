#importando modulo para redirecionar un template html
from django.shortcuts import render,redirect
#importando modulo para obtener respues Http y Json
from django.http import HttpResponse,JsonResponse#jsonResponse se usa para representar un formato de multiple elementos que enetienda el navegador, usdo para los modelos
#importando el modulo para trabajar con con los modelos
from .models import Project,Task
#importando el modulo para el error 404
from django.shortcuts import get_object_or_404 
#importtando el modulo para llamar la clase del formulario del archivo form.py
from .forms import CreateNewTask,CreateNewProject
# Create your views here.

def index(request):
    title = 'Welcome to Django App'
    return render(request,'index.html',{
        'title' : title
    })

def hello(request,username): 
    return HttpResponse(f"<h2>Hello {username}</h2>")
    
def world(request):
    return HttpResponse("<h2>Hello World</h2>")     

def projects(request):
    projec = Project.objects.all()
    return render (request, 'projects/projects.html', {
        'projects' : projec
    })

def tasks(request):
    tasks = Task.objects.all()
    return render (request, 'tasks/task.html', {
        'tasks' : tasks
    })
    
def create_tasks(request):
    if request.method == 'GET':
        # mostrando la interfax si se usa el metodo GET
        return render(request,'tasks/create_tasks.html', {
            'form' : CreateNewTask()
        }) 
    else:
        Task.objects.create(title=request.POST['title'],descripcion=request.POST['descripcion'], project_id_id = 2)
        return redirect('tasks')#al darle nombre a la url se coloca como propiedad 
              
def create_project(request):
    if request.method == 'GET':
        return render(request,'projects/create_project.html', {
            'form' : CreateNewProject()
        })              
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect("project")
        
def project_detail(request,id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id_id=id)
    return render(request, 'projects/detail.html',{
        'project':project,
        'tasks':tasks
    })       