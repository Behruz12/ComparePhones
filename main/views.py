from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class MainIndex(TemplateView):
    template_name = "templates/main/index.html"


