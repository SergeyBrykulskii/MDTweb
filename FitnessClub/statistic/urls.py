from django.urls import path
from . import views

app_name = 'statistic'

urlpatterns = [
    path("analyse", views.analyser, name="analyse")
]