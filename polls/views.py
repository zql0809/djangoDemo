from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
# the view is a controller
from .models import Question
from django.template import loader
from django.shortcuts import render,get_object_or_404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# 和上面对比不使用原始的 HttpResponse template.loader.get_template("页面").render(paramMap,request)这种形式
def index2(request,num):
    lastquestion = Question.objects.order_by("-pub_date")[:5] # 通过年进行排序
    contextList = {"latest_question_list":lastquestion}
    return render(request,'polls/index.html',contextList)

# shortcuts里面封装了一些方便的工具方法 如render替换 template = loader.get_template && template.render('',request)
def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def detail2(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def helloWorld(request):
    return HttpResponse("python study");