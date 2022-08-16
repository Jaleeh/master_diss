from . import views
from django.contrib import admin
from django.urls import include,path



app_name = "attendance"
urlpatterns= [
    path('', views.index, name='index'),
    path('visuals/', views.visuals, name='visuals'),
   ]