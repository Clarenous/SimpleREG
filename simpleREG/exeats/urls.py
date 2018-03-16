from django.urls import path

from . import views

app_name = 'exeats'

urlpatterns = [
    path('', views.exeats, name='exeats'),
    # 展示所有假期的目录
    path('holidays/', views.catalog, name='catalog'),
    # 显示某一假期的详情及当前请假表，页内点击按钮，跳转至填表页面
    path('holidays/<int:holiday_id>/', views.holiday_detail, name='holiday_detail'),
    # 填表页面，提交后跳转回假期详情页面
    path('holidays/<int:holiday_id>/leaveinfo/', views.leaveinfo_edit, name='leaveinfo_edit'),
]

