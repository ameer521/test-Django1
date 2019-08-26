from django.urls import path
from boards import views


urlpatterns = [
    path('',views.home,name="home"),
    path('/new_topic',views.new_topic,name="new_topic"),


]