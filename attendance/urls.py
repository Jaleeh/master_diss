from . import views
from django.contrib import admin
from django.urls import include,path



app_name = "attendance"
urlpatterns= [
    path('', views.index, name='index'),
    path('visuals/', views.visBar, name='visuals'),
    path('boxplot/', views.visBox, name='boxplot'),
    path('averageplot/', views.visAvg, name='averageplot'),
    path('scatterplot/', views.visScatter, name='scatterplot'),
    path('error/', views.errorpage, name='error'),
   ]