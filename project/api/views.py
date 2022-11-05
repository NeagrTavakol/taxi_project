from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from api.models import req_taxi
from .serializers import Req_taxiSerialiser,UserSerialiser
from django.contrib.auth.models import User
from .permissions import IsOwnerOrAuthentication,IsSuperUser,IsSuperUserOrAuthentication

# Create your views here.

class ReqtaxiList(ListCreateAPIView):
    queryset = req_taxi.objects.all()
    serializer_class = Req_taxiSerialiser
    permission_classes = (IsSuperUserOrAuthentication,)

class FilterReqtaxiList(ListCreateAPIView):
    queryset = req_taxi.objects.filter(search_for_taxi=True)
    serializer_class = Req_taxiSerialiser
    permission_classes = (IsSuperUserOrAuthentication,)

class ReqtaxiDetail(RetrieveUpdateDestroyAPIView):
    queryset = req_taxi.objects.all()
    serializer_class = Req_taxiSerialiser
    permission_classes = (IsOwnerOrAuthentication,)
  
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = (IsSuperUser,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = (IsOwnerOrAuthentication,)


class ReqdeliveryList(ListCreateAPIView):
    queryset = req_taxi.objects.filter(type_travel='Taxi' , search_for_taxi=True)
    serializer_class = Req_taxiSerialiser
    permission_classes = (IsSuperUserOrAuthentication,)    


class ReqdeliveryDetail(RetrieveUpdateDestroyAPIView):
    queryset = req_taxi.objects.filter(type_travel='Taxi')
    serializer_class = Req_taxiSerialiser
    permission_classes = (IsOwnerOrAuthentication,)