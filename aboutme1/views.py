
from django.shortcuts import render
from .models import Aboutme1
from django.views.generic import TemplateView

class Viewofaboutme1(TemplateView):
    template_name = "aboutme1.html"
