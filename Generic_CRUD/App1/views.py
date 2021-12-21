from django.shortcuts import render
from .models import Laptop
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class LaptopCreateView(LoginRequiredMixin,CreateView):
    model = Laptop
    fields = '__all__'
    success_url = '/laptop/list/'

class LaptopListView(ListView):
    model = Laptop

class LaptopUpdateView(LoginRequiredMixin,UpdateView):
    model = Laptop
    fields = '__all__'
    success_url = '/laptop/list/'

class LaptopDeleteView(LoginRequiredMixin,DeleteView):
    model = Laptop
    success_url = '/laptop/list/'