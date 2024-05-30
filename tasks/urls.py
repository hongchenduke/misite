from django.urls import path, include, re_path
from . import views

# namespace
app_name = 'tasks'

urlpatterns = [

# """"
#     #视图使用函数视图
#     # 查询任务列表
#     path('', views.task_list, name='task_list'),
#     # 创建一个任务
#     path('create/',views.task_create,name='task_create'),
#     # 查询单个任务
#     re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
#     # 更新单个任务
#     re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
#     # 删除单个任务
#     re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),
# """""
    # 视图使用通用类视图
    # Create a task
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    # Retrieve task list
    path('', views.TaskListView.as_view(), name='task_list'),
    # Retrieve single task object
    re_path(r'^(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='task_detail'),
    # Update a task
    re_path(r'^(?P<pk>\d+)/update/$', views.TaskUpdateView.as_view(), name='task_update'),
    # Delete a task
    re_path(r'^(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(), name='task_delete')
]
