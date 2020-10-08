from django.contrib import admin

# 定义管理页面中不同app中表的数据修改新增
from django.contrib import admin
from .models import Choice,Question

class  ChioceInline(admin.StackedInline):
    model = Choice;
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChioceInline]

admin.site.register(Question, QuestionAdmin)