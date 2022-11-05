from django.urls import path,include
from .views import ReqtaxiList,UserDetail,UserList,FilterReqtaxiList,ReqtaxiDetail

app_name = "api"

urlpatterns = [
    path('all-list',ReqtaxiList.as_view(),name='list'),
    path('reqlist',FilterReqtaxiList.as_view(),name='f_list'),
    path('<int:pk>',ReqtaxiDetail.as_view(),name='detail'),
    path('user/',UserList.as_view(),name='user_list'),
    path('user/<int:pk>',UserDetail.as_view(),name='user_detail'),
]