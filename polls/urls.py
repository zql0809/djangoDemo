from django.urls import path,re_path
from . import views
# 定义poll命名空间 detail2 因为有很多服务都可能有detail同名的view方法
# 所以在这加一个app_name 命名空间
app_name = 'polls'
urlpatterns=[
    # old method for web router
    # path('' ,views.index, name="index"),
    # path('index/<int:num>' ,views.index2, name="index2"),
    # path('<int:question_id>', views.detail, name="detail"),
    # path('index2/<int:question_id>', views.detail2, name="detail2"),
    # path('vote/<int:question_id>',views.vote, name="vote"),
    # path('<int:question_id>/results',views.results, name="results")
    # new method for router 新方法提供给路由

    path('', views.index, name='index'),
    path('list/', views.IndexView.as_view(), name='list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]