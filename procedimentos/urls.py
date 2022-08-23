from django.urls import path
from . import views

urlpatterns = [
    path('procedimentos', views.procedimentos),
]
