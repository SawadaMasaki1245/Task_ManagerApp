from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# タスク一覧を表示するビュー
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# タスクを追加するビュー
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # タスク一覧ページにリダイレクト
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {'form': form})

# タスク編集
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})

# タスク削除
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)  # 指定されたタスクを取得
    if request.method == "POST":  # POSTリクエストが来たら削除
        task.delete()
        return redirect('task_list')  # 削除後にタスク一覧へリダイレクト
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# 完了状況
def task_toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

