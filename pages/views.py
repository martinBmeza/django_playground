from django.shortcuts import render
from django.http import HttpResponse


"""
Usando function-based
def homePageView(request):
    return render(request, 'home.html') #devolviendo un template estatico
    #return HttpResponse('A la grande le puse cuca!') #devolviendo una cadena plana
"""

#usando class based 
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    
class AboutPageView(TemplateView):
    template_name = "about.html"
