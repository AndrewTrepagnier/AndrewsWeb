from django.shortcuts import render
from .models import StartPage
from django.views.generic import TemplateView

class ViewofCover(TemplateView):
    template_name = "coverpage.html"
