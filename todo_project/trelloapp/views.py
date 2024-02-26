from django.shortcuts import render, redirect
from .models import TaskList, Tasks
from .forms import TaskForms
from django.http import JsonResponse

# Create your views here.

def index(request):
    task_list = TaskList.objects.all()
    return render(request, 'trelloapp/index.html', {"tasklist" : task_list})

def showTasks(request, id):
    tasks = Tasks.objects.all()
    showtasks = []
    list_name = ''
    for task in tasks:
        if task.task_list.id == id:
            showtasks.append(task)
            list_name = task.task_list.name
    return render(request, 'trelloapp/showtasks.html', {"tasks": showtasks, "listname": list_name, "id": id})

def create_tasklist(request):
    if request.method == "POST":
        list_name = request.POST['listname']
        task_list = TaskList(name = list_name)
        task_list.save()
        return redirect('index')
    else:
        return render(request, 'trelloapp/newtasklist.html')
    

def create_task_in_tasklist(request, id):
    tsk_lst = TaskList.objects.get(pk = id)
    if request.method == 'POST':
        form = TaskForms(data = request.POST)
        if form.is_valid():
            # task = form.save(commit=False)
            # task.task_list = tsk_lst
            form.instance.task_list = tsk_lst
            form.save()
        return redirect(f'/showtasks/{id}')
    else:
        form = TaskForms()
        return render(request, 'trelloapp/newsingletask.html', {"Form": form})
    

def check_uncheck_checkbox(request):
    # if request.is_ajax():
    taskid = request.POST.get('task_id')
    is_done = request.POST.get('is_done') == 'on'
    print(is_done)
    task = Tasks.objects.get(pk = taskid)
    task.isDone = is_done
    task.save()
    return JsonResponse({'success': True})
