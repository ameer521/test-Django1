from django.shortcuts import render
from django.http import HttpResponse
from .models import Student




# Create your views here.


def home(request):
    return render(request,'blog/test.html')


