from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Moviesdetail

# Create your views here.
def index(request):
    # return HttpResponse("Hi Welcome to Home Page")
    templates = loader.get_template('home.html')
    return HttpResponse(templates.render())
