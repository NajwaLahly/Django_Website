from django.urls import path
from . import views


urlpatterns = [
    path('', views.AI_home, name='AI_home'),
]