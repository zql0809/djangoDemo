from django.db import models
from django.utils import timezone
import datetime


# 问题表
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # 校验问题发布时间是不是在最近一天
    def was_published_recently(self):
        now = timezone.now()
        boola = now - datetime.timedelta(days=1) <= self.pub_date<= now;
        boolb = now <= self.pub_date <= now + datetime.timedelta(days=1);
        return boola or boolb;

    def __str__(self):
        return self.question_text


# 投票表
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text