from django.urls import path,include
from .views import Req_taxiList,Req_taxiDetail

app_name = "taxiapp"
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('',Req_taxiList.as_view(),name='list'),
    path("<int:pk>",Req_taxiDetail.as_view(),name='detail'),
]
