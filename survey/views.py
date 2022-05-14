from django.shortcuts import render
from django.views.generic import TemplateView


class SurveyPageView(TemplateView):
    template_name = "survey.html"
    