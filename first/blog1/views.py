from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fetch_template(request):
    return HttpResponse("Hey")
