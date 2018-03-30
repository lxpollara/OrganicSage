
from django.conf.urls import url, handler404
from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.MapPageView.as_view()),
    path('basemap/', views.BaseMapPageView.as_view()),
]
