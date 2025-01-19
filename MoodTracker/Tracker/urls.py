from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('log_mood/', views.log_mood, name='log_mood') 
]