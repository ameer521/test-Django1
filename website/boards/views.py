from django.shortcuts import render
from django.http import HttpResponse
from .models import *



# Create your views here.


def home(request):
    boards = Boards.objects.all()
    return render(request,'home.html',{'boards':boards})
    #boards_names = []


   # for i in boards:
     #   boards_names.append(i.name)

  #  response_html = "<br>The names are <br>".join(boards_names)


   # return HttpResponse(response_html)

