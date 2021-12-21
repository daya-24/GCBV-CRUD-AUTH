from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('show_lap')
        else:
            messages.error(request, 'Invalid Credentials !')
    context = {}
    template_name = 'Accounts/login.html'
    return render(request, template_name, context)

def registerView(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login1')

    context = {'form': form}
    templates_name = 'Accounts/register.html'
    return render(request, templates_name, context)

def logoutView(request):
    logout(request)
    return redirect('login1')