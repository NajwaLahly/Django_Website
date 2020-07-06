from django.urls import path
from . import views


urlpatterns = [
    path('', views.path_finding_home, name='path_finding_home'),
]