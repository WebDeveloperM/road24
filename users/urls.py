from django.urls import path
from .views import *
urlpatterns = [
    path('' , sign_up, name='sign_up'),
    path('sign_out' , sign_out, name='sign_out')

]
