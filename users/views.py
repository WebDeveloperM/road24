from django.shortcuts import render,redirect
from django.contrib.auth import  logout

# Create your views here.


def sign_up(request):
    pass

def sign_out(request):
    logout(request)
    return redirect("avtorizatsiya")