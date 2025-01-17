from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 

class Task(models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField()
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.project_id.name