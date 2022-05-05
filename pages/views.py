from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('A la grande le puse cuca!')
# Create your views here.
