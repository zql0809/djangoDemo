from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
# the view is a controller
from .models import Question,Choice
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

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


# 实际某些操作的action方法
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.  302跳转
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# 重构上面的方法 2020-09-25 每个实体都会有getDetail getList
from django.views import generic

# 公共列表方法
class IndexView(generic.ListView):
    template_name = "polls/list.html"  # 需要跳转的页面配置
    context_object_name = "latest_question_list" # 送到页面的参数map

    def get_queryset(self):
        """Return the last five published questions. 返回的展示数据"""
        return Question.objects.order_by('-pub_date')[:5]

# 公共详细页面
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# 公共投票结果页面
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# 首页
def index(request):
    return render(request,'polls/index.html');