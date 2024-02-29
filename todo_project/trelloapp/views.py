from django.shortcuts import render, redirect
from .models import TaskList, Tasks
from .forms import TaskForms
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')
def index(request):
    task_list = TaskList.objects.filter(user = request.user)
    return render(request, 'trelloapp/index.html', {"tasklist" : task_list})

@login_required(login_url = 'login')
def showTasks(request, id, listname):
    tasks = Tasks.objects.all()
    showtasks = []
    list_name = listname
    for task in tasks:
        if task.task_list.id == id:
            showtasks.append(task)
            list_name = task.task_list.name
    return render(request, 'trelloapp/showtasks.html', {"tasks": showtasks, "listname": list_name, "id": id})

@login_required(login_url = 'login')
def create_tasklist(request):
    if request.method == "POST":
        list_name = request.POST['listname']
        myuser = request.user
        task_list = TaskList(name = list_name, user = myuser)
        task_list.save()
        return redirect('index')
    else:
        return render(request, 'trelloapp/newtasklist.html')
    
@login_required(login_url = 'login')
def create_task_in_tasklist(request, id):
    tsk_lst = TaskList.objects.get(pk = id)
    if request.method == 'POST':
        form = TaskForms(data = request.POST)
        if form.is_valid():
            # task = form.save(commit=False)
            # task.task_list = tsk_lst
            form.instance.task_list = tsk_lst
            form.save()
        return redirect(f'/showtasks/{id}/{tsk_lst.name}')
    else:
        form = TaskForms()
        return render(request, 'trelloapp/newsingletask.html', {"Form": form, "id": id, "taskid": 1, "is_update": False})
    
@login_required(login_url = 'login')
def check_uncheck_checkbox(request):
    # if request.is_ajax():
    taskid = request.POST.get('task_id')
    is_done = request.POST.get('is_done') == 'on'
    # print(is_done)
    task = Tasks.objects.get(pk = taskid)
    task.isDone = is_done
    task.save()
    return JsonResponse({'success': True})

@login_required(login_url='login')
def update_task(request, id):
    task = Tasks.objects.get(pk = id)
    if request.method == "POST":
        form = TaskForms(data = request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect(f'/showtasks/{task.task_list.id}/{task.task_list.name}')
    form = TaskForms(instance = task)
    return render(request, 'trelloapp/newsingletask.html', {"Form": form, "id": task.task_list.id, "taskid": id, "is_update": True})

@login_required(login_url='login')
def delete_task(request, id):
    task = Tasks.objects.get(pk = id)
    task.delete()
    return redirect(f'/showtasks/{task.task_list.id}/{task.task_list.name}')

@login_required(login_url='login')
def delete_list(request, id):
    tasklist = TaskList.objects.get(pk = id)
    tasklist.delete()
    return redirect('index')
