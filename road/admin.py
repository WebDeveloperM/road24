from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['number', 'is_active']
    fields = ['model', "number",'teck_number','brand','image', 'user','is_active']

admin.site.register(Card)

admin.site.register(Fine)
# @admin.register(Fine)
# class FineAdmin(admin.ModelAdmin):
#     list_display = ['car', 'violation_date']
#     fields = [
#         'car','decision_number','violation_date','decision_date','violation_clause','violation_description','violation_address','fine_amount','fine_fast','fine_image','is_payment',
#   ]
