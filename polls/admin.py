from django.contrib import admin

# 定义管理页面中不同app中表的数据修改新增
from django.contrib import admin
from .models import Question
admin.site.register(Question)