from django.urls import path
from .views import SurveyPageView

urlpatterns = [
    path("", SurveyPageView.as_view(), name = 'forms')
]