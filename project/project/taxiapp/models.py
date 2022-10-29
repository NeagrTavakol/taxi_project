from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class req_taxi(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    orig_addr = models.CharField(max_length=1000)
    dest_addr = models.CharField(max_length=1000)
    search_for_taxi = models.BooleanField(default = True)
    achieve_dest = models.BooleanField(default= False)
    travel_costs = models.IntegerField()

    def __str__(self):
        return self.orig_addr