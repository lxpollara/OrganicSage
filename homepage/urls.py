
from django.conf.urls import url, handler404
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('biography/', views.BioPageView.as_view()),
    path('services/', views.ServicesPageView.as_view()),
    path('contact/', views.ContactPageView.as_view()),
    path('qualifications/', views.QualificationsPageView.as_view()),
    path('construction/', views.ConstructionPageView.as_view()),
]

handler404 = views.error_404.as_view()
