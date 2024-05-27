#importando modulo para path
from django.urls import path
#importando las vistas
from . import views #el . indica que estamos en la misma carpeta

#creando lista para modulos direcciones path
urlpatterns = [
    path('',views.index,name = "index"),
    path('hello/',views.world),
    path('hello/<str:username>',views.hello),
    path('projects/',views.projects, name = "project"),
    path('projects/<int:id>',views.project_detail , name = "project_detail"),
    path('tasks/',views.tasks, name = "tasks"),
    path('create_new_tasks/',views.create_tasks , name = "create_tasks"),
    path('create_project',views.create_project , name = "create_project"),
    
]
