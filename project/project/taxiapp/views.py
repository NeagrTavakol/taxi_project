import imp
from django.views.generic import ListView,DeleteView
from .models import req_taxi
from django.shortcuts import get_object_or_404

# Create your views here.

class Req_taxiList(ListView):
    def get_queryset(self):
        return req_taxi.objects.all()

class Req_taxiDetail(DeleteView):
    def get_object(self):
        return get_object_or_404(req_taxi,pk=self.kwargs.get("pk"))
