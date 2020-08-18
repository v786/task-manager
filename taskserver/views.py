from django.shortcuts import render
from django.views import View
from .models import TaskServer, Task

# Create your views here.
def fetch_context():
    context = {}
    context["tasklist"] = TaskServer.objects.all()

    return context

def get(request):
    context = fetch_context()
    return render(request, 'taskserver/index.html', context)


def post(request):
    context = fetch_context()
    servers_count = len(context["tasklist"])
    new_server_name = "Server"+str(servers_count)
    task_server = TaskServer(description=new_server_name)
    task_server.save()
    
    return render(request, 'taskserver/index.html', context)

def delete(request, server_id):
    context = fetch_context()
    task_server = TaskServer.objects.get(pk=server_id)
    task_server.delete()    
    return render(request, 'taskserver/index.html', context)

def add_task(request, server_id):
    context = fetch_context()
    task_server = TaskServer.objects.get(pk=server_id)
    count = len(Task.objects.all())
    name = "Task"+str(count)
    task = Task(title= name,active= False,completed= False,server= task_server)
    task.save()
    flag = True
    for task in task_server.task_set.all():
        if task.active:
            flag = False
            break
    if flag:
        task.active = True
        task.save()
    return render(request, 'taskserver/index.html', context)