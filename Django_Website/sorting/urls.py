from django.urls import path
from . import views


urlpatterns = [
    path('', views.sorting_home, name='sorting_home'),
]