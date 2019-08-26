from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.


def show(request):
    return render(request,'shop/index.html')

def home(request):
    return render(request,'shop/index.html')

def news(request):
    return render(request,'shop/news.html')