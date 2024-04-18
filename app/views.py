from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import *

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Home(TemplateView):
    template_name = 'index.html'



def shop(request):
    return render(request, 'shop.html', context={})

def detail(request):
    return render(request, 'details.html', context={})

def compare(request):
    return render(request, 'compare.html', context={})

def accounts(request):
    return render(request, 'accounts.html', context={})

