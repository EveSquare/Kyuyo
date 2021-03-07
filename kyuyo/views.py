from django.shortcuts import render

from django.views import generic

# Create your views here.
class Dashboard(generic.TemplateView):
    template_name = 'kyuyo/dashborad.html'