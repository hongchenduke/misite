from django.contrib import admin
from .models import Task


# Register your models here.

# 定义task app在admin后台的展示
class TaskAdmin(admin.ModelAdmin):
    # 展示字段
    list_display = ['name', 'status']
    # 可编辑字段
    list_editable = ('status',)
    # 每页展示条数
    list_per_page = 5
    # 可搜索字段
    search_fields = ['name']


# 注册task app至后台admin
admin.site.register(Task, TaskAdmin)
