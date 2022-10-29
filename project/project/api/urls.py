from django.urls import path,include
from .views import ReqtaxiList,ReqtaxiDetail,UserDetail,UserList

app_name = "api"

urlpatterns = [
    path('',ReqtaxiList.as_view(),name='list'),
    path('<int:pk>',ReqtaxiDetail.as_view(),name='detail'),
    path('user/',UserList.as_view(),name='user_list'),
    path('user/<int:pk>',UserDetail.as_view(),name='user_detail'),
]