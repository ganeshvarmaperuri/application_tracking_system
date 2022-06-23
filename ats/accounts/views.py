from django.shortcuts import render
from django.views.generic import TemplateView


class Dashboard(TemplateView):
    template_name = 'home.html'


class Login(TemplateView):
    template_name = 'authentication/login.html'
