from tempfile import template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

from .models import Snack


# Create your views here.
class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = "snack_list"

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'
