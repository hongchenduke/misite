""" 使用函数视图
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task
from .forms import TaskForm


# Create your views here.
# 查询任务列表
def task_list(request):
    # 从数据库获取Task对象列表
    tasks = Task.objects.all()
    # 指定渲染模板并向模版传递数据
    return render(request, "tasks/task_list.html", {"tasks": tasks, })


# 创建一个任务
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_list"))
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form, })


# 查询单个任务
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task, })


# 更新单个任务
def task_update(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(instance=task_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_detail", args=[pk, ]))
    else:
        form = TaskForm(instance=task_obj)
    return render(request, "tasks/task_form.html", {"form": form, "object": task_obj})


# 删除单个任务

def task_delete(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    task_obj.delete()
    return redirect(reverse("tasks:task_list"))
"""

# 使用通用实现
from django.urls import reverse, reverse_lazy
from .models import Task
from .forms import TaskForm
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:task_list')