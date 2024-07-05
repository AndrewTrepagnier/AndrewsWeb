from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Aboutme


# def Aboutme_view(request):
#     posts = Aboutme.objects.all().order_by('-date')
#     return render(request, 'aboutme.html', {'posts': posts})
class Aboutme(TemplateView):
     template_name = "aboutme.html"

