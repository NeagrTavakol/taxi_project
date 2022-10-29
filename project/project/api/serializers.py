from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from taxiapp.models import req_taxi
from django.contrib.auth.models import User


class Req_taxiSerialiser(serializers.ModelSerializer):
    class Meta:
        model = req_taxi
        fields = ("user","orig_addr","dest_addr","search_for_taxi","achieve_dest","travel_costs")

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
