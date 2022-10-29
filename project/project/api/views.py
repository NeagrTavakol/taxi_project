from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from taxiapp.views import req_taxi
from rest_framework.permissions import IsAdminUser
from .serializers import Req_taxiSerialiser,UserSerialiser
from django.contrib.auth.models import User

# Create your views here.

class ReqtaxiList(ListCreateAPIView):
    queryset = req_taxi.objects.all()
    serializer_class = Req_taxiSerialiser

class ReqtaxiDetail(RetrieveAPIView):
    queryset = req_taxi.objects.all()
    serializer_class = Req_taxiSerialiser
  
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = (IsAdminUser,)

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = (IsAdminUser,)