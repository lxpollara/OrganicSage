from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.
class MapPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'projects.html', context=None)


class BaseMapPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'map.html', context=None)
