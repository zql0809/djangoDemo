from django.urls import path,re_path
from . import views
# 定义poll命名空间 detail2 因为有很多服务都可能有detail同名的view方法
# 所以在这加一个app_name 命名空间
app_name = 'polls'
urlpatterns=[
    path('hello/wrold', views.helloWorld, name="hello"),
    # path('' ,views.index, name="index"),
    path('index/<int:num>' ,views.index2, name="index2"),
    path('<int:question_id>', views.detail, name="detail"),
    path('index2/<int:question_id>', views.detail2, name="detail2"),
    path('vote/<int:question_id>',views.vote, name="vote"),
    path('<int:question_id>/results',views.results, name="results")
]