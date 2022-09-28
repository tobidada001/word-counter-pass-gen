from django.urls import path
from helloapp import views

urlpatterns = [
    path('', views.indexpage),
    path('page', views.loadnewpage),
]