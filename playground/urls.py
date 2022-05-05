from django.urls import path
from . import views #para poder referenciar mis vistas

#URL config
urlpatterns = [
    path('hello/', views.say_hello)
]