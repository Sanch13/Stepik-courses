from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.GreetingView.as_view(), name="hello")
]
