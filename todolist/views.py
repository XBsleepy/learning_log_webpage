from django.shortcuts import render,redirect
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from .models import Task
from django.utils import timezone
from django.http import JsonResponse
# Create your views here.
@login_required
def list_todo(request):
    # 获取所有待办事项，并按照重要性和紧急程度进行分类和排序
    important_emergency = Task.objects.filter(is_important=True, is_urgent=True).order_by('due_date')
    important_non_emergency = Task.objects.filter(is_important=True, is_urgent=False).order_by('due_date')
    non_important_emergency = Task.objects.filter(is_important=False, is_urgent=True).order_by('due_date')
    non_important_non_emergency = Task.objects.filter(is_important=False, is_urgent=False).order_by('due_date')
    now=timezone.now()
    context = {
        'important_emergency': important_emergency,
        'important_non_emergency': important_non_emergency,
        'non_important_emergency': non_important_emergency,
        'non_important_non_emergency': non_important_non_emergency,
        'now': now,
    }

    return render(request, 'todolist/list_todo.html', context)
@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            if not new_task.due_date:
                new_task.due_date = timezone.now()  # 设置默认的 due_date
            new_task.save()
            return redirect('todolist:list_todo')
    else:
        form = TaskForm()

    context = {'form': form}
    return render(request, 'todolist/add_todo.html', context)
@login_required
def toggle_complete(request, task_id): 
    task = Task.objects.get(id=task_id)     
    task.complete = not task.complete    
    task.save()     
    return JsonResponse({'complete': task.complete})