from django.urls import path
from . import views

urlpattern = [
      path('', views.test_endpoint, name="test_endpoint")
]