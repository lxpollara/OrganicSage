from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Qualifications, Services


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class BioPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'bio.html', context=None)


class ServicesPageView(TemplateView):
    def get(self, request, **kwargs):
        services = Services.objects.order_by('published_date')
        return render(request, 'services.html', {'services': services})


class ContactPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'contact.html', context=None)


class QualificationsPageView(TemplateView):
    def get(self, request, **kwargs):
        quals = Qualifications.objects.order_by('published_date')
        return render(request, 'qualifications.html', {'quals': quals})


class ConstructionPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'construction.html', context=None)


class error_404(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'construction.html', context=None)
