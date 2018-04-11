from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import ProjectLoc
from .mapmaker import map_gen

# Create your views here.
class MapPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'projects.html', context=None)


class BaseMapPageView(TemplateView):
    def get(self, request, **kwargs):
        proj = ProjectLoc.objects.all()
        map_gen(proj)
        return render(request, 'map.html', context=None)

#TODO make mapmaker output html dirtectly into posts
