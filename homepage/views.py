from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class BioPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'bio.html', context=None)


class ServicesPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'services.html', context=None)


class ConstructionPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'construction.html', context=None)


class error_404(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'construction.html', context=None)
