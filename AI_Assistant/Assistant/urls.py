from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
  path('explore/', views.explore, name='explore'),
  path('object/', views.object_detection, name='object_detection'),
  path('weather/', views.weather, name='weather'),
  

]


