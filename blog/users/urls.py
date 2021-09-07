# 进行users 子应用的视图路由

from django.urls import path
from . import views


urlpatterns = [
    # 第一个参数：路由
    # 第二个参数：视图函数名
    path('register/', views.RegisterView.as_view(), name='register'),
]
