from django.db import models

# Create your models here.

class TaskServer(models.Model):
    description = models.TextField()

    def add_task(self):
        return

    def __str__(self):
        return self.description

class Task(models.Model):
    title = models.TextField(max_length=100, default="Task")
    active = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    server = models.ForeignKey(TaskServer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title