from django.shortcuts import render
from .models import Task


# Create your views here.

# 任务清单
def task_list(request):
    # 从数据库获取Task对象列表
    tasks = Task.objects.all()
    # 指定渲染模板并向模版传递数据
    return render(request, "tasks/task_list.html", {"tasks": tasks, })
