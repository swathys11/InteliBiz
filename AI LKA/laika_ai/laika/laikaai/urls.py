# urls.py (App Level)

from django.urls import path
from . import views
from .views import email_view

urlpatterns = [
    path('', views.index, name='index'),
    path('explore/', views.explore, name='explore'),
    # path('process_command/', views.process_command, name='process_command'),
    path('email_assistant/', views.email_assistant, name='email_assistant'),
    path('object/', views.object_detection_view, name='object_detection'),
    path('weather/', views.weather_view, name='weather'),
     path('email/', views.email_view, name='email'),
     path('current_time/', views.get_current_time_view, name='current_time'),
     path('process_command/', views.process_command, name='process_command'),
      path('get_joke/', views.get_joke, name='get_joke'),
     
    
     
]
        


