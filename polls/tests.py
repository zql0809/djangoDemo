from django.test import TestCase
from django.utils import timezone
from .models import Question
import  datetime
# 单元测试
# Create your tests here.
class QuestionTest(TestCase):
    def test1(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

