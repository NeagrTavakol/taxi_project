from django.contrib import admin
from .models import req_taxi
 
# @admin.register(req_taxi)
# class Reqtaxiadmin(admin.ModelAdmin):
#   list_display = ['user', 'orig_addr','dest_addr','search_for_taxi','achieve_dest','travel_costs','type_travel']
admin.site.register(req_taxi)