from django.shortcuts import render
from django.views.generic import TemplateView


class MixerView(TemplateView):
    template_name = 'index.html'