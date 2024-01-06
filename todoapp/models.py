from django.db import models

# Create your models here.
class Project(models.Model):
    nombre = models.CharField(max_length=200)
    decripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Task(models.Model):
    titulo = models.CharField(max_length=200)
    decripcion = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo + ' - Nombre del projecto: ' + self.project.nombre

