from django.urls import path
from . import views


urlpatterns = [
    path('',views.show,name='show'),
    path('home/',views.home,name='home'),
    path('news/',views.news,name='news'),
]